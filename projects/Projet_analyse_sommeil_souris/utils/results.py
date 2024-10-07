from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import cohen_kappa_score

def scores(y_true, y_pred, labels):
  report(y_true, y_pred, labels)
  cohen_kappa(y_true, y_pred)
  conf_matrix(y_true, y_pred, labels)
  
def conf_matrix(y_true, y_pred, labels):
  print("Matrice de confusion :")
  cm = confusion_matrix(y_true, y_pred)
  disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
  disp.plot(xticks_rotation='vertical')
  
def report(y_true, y_pred, labels):
  print("Rapport de classification : ")
  print(classification_report(y_true, y_pred, target_names=labels))
  
def cohen_kappa(y_true, y_pred):
  print("Coefficient de cohen's kappa : " + str(cohen_kappa_score(y_true, y_pred)))