from PyQt5.QtWidgets import QWidget, QMessageBox
import Wydbid
from Data import DataCombi

def delEmployeeFinal(username: str, password: str, widget: QWidget):
    if username == '' or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return

    session = DataCombi.session(bind=DataCombi.engine)

    employee = session.query(DataCombi.Employee).filter(DataCombi.Employee.username == username).first()
    print(employee)

    return

    if not password == employee.password:
        QMessageBox.warning(Wydbid.app.parent(), 'Attention',
                            'Attention, the password entered is incorrect!')
        return

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      'The employee has been deleted!')
