from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class Metrics:
    def __init__(self, y_test, y_pred):
        self.y_test = y_test
        self.y_pred = y_pred

    def calculate(self):
        print()
        
        print('Total test items:', len(self.y_test))
        print()

        # Accuracy
        accuracy = accuracy_score(self.y_test, self.y_pred)
        print('Accuracy:', accuracy)
        print()

        # Calcule Precision score using sklearn.metrics
        precision = precision_score(self.y_test, self.y_pred)
        print('Precision:', precision)
        print()

        # Calcule Precision score using sklearn.metrics
        recall = recall_score(self.y_test, self.y_pred)
        print('Recall:', recall)
        print()

        # Calcule F1 score using sklearn.metrics
        recall = f1_score(self.y_test, self.y_pred)
        print('F1 Score:', recall)
        print()
