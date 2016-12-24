import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from scriptGenerator import ScriptGenerator
import scraper

class MainWindow(QMainWindow):
    """ The class that defines the structure of the application's GUI.
    """
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)

        self.menubar = self.menuBar()
        file_ = self.menubar.addMenu("File")
        edit = self.menubar.addMenu("Edit")

        self.dialog = QDialog()

        self.statusbar = self.statusBar()

        mainlayout = QVBoxLayout()
        grid = QGridLayout()

        self.urlLabel = QLabel("URL:")
        self.urlInput = QLineEdit()
        self.selectorLabel = QLabel("Selector:")
        self.selectorInput = QLineEdit()
        self.button = QPushButton()
        self.button.setText("Scrape It")
        self.button.setFixedWidth(100)
        self.button.clicked.connect(self.modifyUI)

        grid.addWidget(self.urlLabel,0,0)
        grid.addWidget(self.urlInput,0,1)
        grid.addWidget(self.selectorLabel,1,0)
        grid.addWidget(self.selectorInput,1,1)
        grid.addWidget(self.button,2,1)

        mainlayout.addLayout(grid)

        self.tab = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab.addTab(self.tab1, "1")
        self.tab.addTab(self.tab2,"2")
        self.tab.addTab(self.tab3,"3")

        tab1layout = QVBoxLayout()
        self.scriptBrowser = QTextBrowser()
        self.scriptBrowser.append("")
        tab1layout.addWidget(self.scriptBrowser)
        self.tab.setTabText(0,"Python Script")
        self.tab1.setLayout(tab1layout)

        tab2layout = QVBoxLayout()
        self.web = QWebView()
        tab2layout.addWidget(self.web)
        self.tab.setTabText(1,"Webpage")
        self.tab2.setLayout(tab2layout)

        tab3layout = QVBoxLayout()
        self.dataBrowser = QTextBrowser()
        self.dataBrowser.append("Scraped Data: \n\n")
        tab3layout.addWidget(self.dataBrowser)
        self.tab.setTabText(2,"Scraped Data")
        self.tab3.setLayout(tab3layout)

        mainlayout.addWidget(self.tab)
        self.dialog.setLayout(mainlayout)
        self.setCentralWidget(self.dialog)

    def modifyUI(self):
        """ Method to modify UIs for the tabs after scraping.
        """
        message = QMessageBox();
        message.setIcon(QMessageBox.Information)
        message.setText("Scraping under progress...")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.exec_()
        url = self.urlInput.text()
        selectors = self.selectorInput.text()
        sc = scraper.Scraper(str(url),str(selectors))
        scr = ScriptGenerator(url,selectors).generate()
        self.web.load(QUrl(url))
        print "Webpage Loaded \n"
        sc.parse()
        print "Scrapping done"
        self.dataBrowser.append(str(sc.data))
        self.scriptBrowser.append(str(scr))
        return

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

# modifyUI() method to be changed for cheking input and displaying required info
# Layouts may be made better
# Menu bar will be modified
# About section to be included
