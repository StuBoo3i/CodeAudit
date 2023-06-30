import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建布局和视图
        layout = QVBoxLayout()
        tree_view = QTreeView()

        # 创建文件系统模型
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['File Name'])

        # 获取根目录
        root_path = QDir.currentPath()

        # 构建文件树
        self.build_file_tree(model, root_path)

        # 设置模型和视图
        tree_view.setModel(model)
        tree_view.clicked.connect(self.on_tree_item_clicked)

        # 添加视图到布局
        layout.addWidget(tree_view)

        # 创建中心部件并设置布局
        central_widget = QMainWindow()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def build_file_tree(self, model, path):
        stack = [(model.invisibleRootItem(), path)]

        while stack:
            parent_item, current_path = stack.pop()

            dir_entries = QDir(current_path).entryInfoList()

            for entry in dir_entries:
                if entry.isDir() and not entry.isHidden():
                    # 创建目录项
                    dir_item = QStandardItem(entry.fileName())
                    dir_item.setIcon(QIcon().fromTheme("folder"))
                    dir_item.setSelectable(False)

                    # 添加目录项到父项
                    parent_item.appendRow(dir_item)

                    # 将子目录入栈
                    stack.append((dir_item, entry.filePath()))
                elif entry.isFile() and not entry.isHidden():
                    # 创建文件项
                    file_item = QStandardItem(entry.fileName())
                    file_item.setIcon(QIcon().fromTheme("document"))
                    file_item.setData(entry.filePath(), Qt.UserRole)

                    # 添加文件项到父项
                    parent_item.appendRow(file_item)

    def on_tree_item_clicked(self, index):
        # 获取点击的项
        item = index.model().itemFromIndex(index)

        # 检查是否为文件项
        if item.data(Qt.UserRole):
            file_path = item.data(Qt.UserRole)
            self.open_file(file_path)

    def open_file(self, file_path):
        # 在这里实现打开文件的逻辑
        print(f"Opening file: {file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
