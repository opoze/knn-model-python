-- View: mimiciii.vitals

-- DROP MATERIALIZED VIEW IF EXISTS mimiciii.vitals;

CREATE MATERIALIZED VIEW IF NOT EXISTS mimiciii.vitals
TABLESPACE pg_default
AS
 SELECT pvt2.time_stamp,
    pvt2.patient_id,
    pvt2.admission_id,
    pvt2.heart_rate,
    pvt2.temperature,
    pvt2.spo2,
        CASE
            WHEN pvt2.heart_rate >= 60::numeric AND pvt2.heart_rate <= 100::numeric AND pvt2.spo2 >= 95::numeric AND pvt2.temperature >= 36.5 AND pvt2.temperature <= 37.4 THEN 0
            ELSE 1
        END AS label
   FROM ( SELECT pvt.charttime AS time_stamp,
            pvt.subject_id AS patient_id,
            pvt.hadm_id AS admission_id,
            round(max(
                CASE
                    WHEN pvt.vitalid = 1 THEN pvt.valuenum::numeric
                    ELSE NULL::numeric
                END), 2) AS heart_rate,
            round(max(
                CASE
                    WHEN pvt.vitalid = 2 THEN pvt.valuenum::numeric
                    ELSE NULL::numeric
                END), 2) AS temperature,
            round(max(
                CASE
                    WHEN pvt.vitalid = 3 THEN pvt.valuenum::numeric
                    ELSE NULL::numeric
                END), 2) AS spo2
           FROM ( SELECT ie.subject_id,
                    ie.hadm_id,
                    ie.icustay_id,
                    ce.valuenum,
                    ce.charttime,
                        CASE
                            WHEN (ce.itemid = ANY (ARRAY[211, 220045])) AND ce.valuenum > 0::double precision AND ce.valuenum < 300::double precision THEN 1
                            WHEN (ce.itemid = ANY (ARRAY[223762, 676])) AND ce.valuenum > 10::double precision AND ce.valuenum < 50::double precision THEN 2
                            WHEN (ce.itemid = ANY (ARRAY[646, 220277])) AND ce.valuenum > 0::double precision AND ce.valuenum <= 100::double precision THEN 3
                            ELSE NULL::integer
                        END AS vitalid
                   FROM mimiciii.icustays ie
                     LEFT JOIN mimiciii.chartevents ce ON ie.subject_id = ce.subject_id AND ie.hadm_id = ce.hadm_id AND ie.icustay_id = ce.icustay_id AND ce.charttime >= ie.intime AND ce.error IS DISTINCT FROM 1
                  WHERE ce.itemid = ANY (ARRAY[211, 220045, 646, 220277, 676, 223761])) pvt
          GROUP BY pvt.charttime, pvt.subject_id, pvt.hadm_id, pvt.icustay_id) pvt2
  WHERE pvt2.heart_rate IS NOT NULL AND pvt2.temperature IS NOT NULL AND pvt2.spo2 IS NOT NULL
WITH DATA;

ALTER TABLE IF EXISTS mimiciii.vitals
    OWNER TO lpozenato;