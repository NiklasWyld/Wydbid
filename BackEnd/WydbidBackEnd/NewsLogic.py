from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from sqlalchemy.orm import sessionmaker
from Data.DataCombi import *
import Wydbid

def createNewsFinal(widget):
    title = widget.title.text()
    description = widget.description.toPlainText()

    if title == '':
        QMessageBox.warning(Wydbid.app.parent(), 'Warning',
                            'At least the title field must be filled in.')
        return

    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    news = News(title, description)

    session.add(news)
    session.commit()

    QMessageBox.about(widget, 'Completed',
                      f'{news.title} was created.')

    widget.clear()
    widget.hide()

def appendNews(newslist: QListWidget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    newslist.clear()

    news = session.query(News).all()

    for _news in news:
        item = QListWidgetItem(parent=newslist)

        item.setText(_news.title)
        item.setData(Qt.UserRole, _news.id)

        newslist.addItem(item)

    session.commit()

def getNews(news):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    _news = session.query(News).filter(News.id == news).first()

    return _news