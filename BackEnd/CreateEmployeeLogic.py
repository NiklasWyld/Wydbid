from PyQt5.QtWidgets import QMessageBox, QWidget
import Wydbid
from Data.DataCombi import session, engine, Employee

def createEmployeeFinal(name: str, username: str, password: str, widget: QWidget):
    if name == '' or username == '' or password == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'All fields must be filled in!')
        return
    print(Wydbid.company_location)
    my_session = session(bind=engine)

    # Check if employee already exists
    for employee in my_session.query(Employee).all():
        if employee.username == username:
            QMessageBox.warning(Wydbid.app.parent(), 'Attention', 'A employee with this user name already exists.')
            return

    employee = Employee(username, name, password)

    my_session.add(employee)
    my_session.commit()

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      f'{name} was created.')