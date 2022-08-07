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

    Wydbid.wydbidui.setLatestNews()

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

    # Get news from id in data
    _news = session.query(News).filter(News.id == news).first()

    return _news

def delNews(news_list: QListWidget, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    if not news_list.selectedItems():
        QMessageBox.warning(widget, 'Warning',
                            'No news selected!')
        return

    news_id = news_list.selectedItems()[0].data(Qt.UserRole)

    news = session.query(News).filter(News.id == news_id).first()

    reply = QMessageBox.question(widget, 'Are you sure?', f'Are you sure you want to delete {news.title}?',
                                 QMessageBox.Yes, QMessageBox.No)

    if reply == QMessageBox.No:
        QMessageBox.about(Wydbid.app.parent(), 'Cancled',
                          'The news has not been deleted!')
        session.commit()
        return

    session.delete(news)
    session.commit()

    QMessageBox.about(Wydbid.app.parent(), 'Completed',
                      'The news has been deleted!')

    widget.hide()
    Wydbid.wydbidui.setLatestNews()

def setNewsForEdit(news_id, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    news = session.query(News).filter(News.id == news_id).first()

    widget.setNewsFinal(news)

    session.commit()

def editNews(news_id, title, description, widget):
    engine = create_engine(f'sqlite:///{Wydbid.company_location}database.db')
    _session = sessionmaker()
    session = _session(bind=engine)

    base.metadata.create_all(engine)

    session.query(News).filter(News.id == news_id).update(
        {
            News.title: title,
            News.description: description
        }
    )

    session.commit()

    QMessageBox.about(Wydbid.app.parent(), 'Process completed',
                      f'{title} has been successfully updated.')

    widget.clear()
    widget.hide()

    Wydbid.wydbidui.setLatestNews()