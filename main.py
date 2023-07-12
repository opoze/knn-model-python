from application import Application

START_MSG = 'Starting...'
FINISH_MSG = '...Finish'

if __name__ == "__main__":
    print(START_MSG)

    Application().run()

    print(FINISH_MSG)
