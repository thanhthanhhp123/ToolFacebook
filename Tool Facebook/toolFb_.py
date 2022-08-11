from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QFont
import requests
import fb
import ProcessingAPI as pa

font = QFont('Times New Roman', 16)
font1 = QFont('Times', 16)

class PostWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Auto Post')
		self.setGeometry(50, 50, 400, 400)
		self.UI()

	def UI(self):
		self.l_cookies = QLabel('Your cookies: ', self)
		self.l_cookies.move(50, 30)
		self.l_cookies.setFont(font)

		self.cookies = QLineEdit(self)
		self.cookies.setPlaceholderText('Enter your cookies: ')
		self.cookies.move(150, 30)

		self.l_content = QLabel('Content: ', self)
		self.l_content.setFont(font)
		self.l_content.move(70, 60)

		self.content = QLineEdit(self)
		self.content.setPlaceholderText('Enter the content: ')
		self.content.move(150, 60)

		self.l_spinBox = QLabel('Quantity: ', self)
		self.l_spinBox.move(70, 90)
		self.l_spinBox.setFont(font)

		self.spinBox = QSpinBox(self)
		self.spinBox.move(150, 90)
		self.spinBox.setMaximum(10000)

		button = QPushButton('Post', self)
		button.move(150, 120)
		button.clicked.connect(self.post)

		self.show()

	def post(self):
		cookies = self.cookies.text()
		content = self.content.text()
		quantity = self.spinBox.value()
		c_json = pa.convert_cookie_to_json(cookies)
		fb_dtsg = pa.get_fb_dtsg(c_json)
		fb.autoPostStatus(content, quantity, fb_dtsg, c_json)

class spamTimeline(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(50, 50, 400, 400)
		self.setWindowTitle('Spam Timeline Of Friend')
		self.UI()

	def UI(self):
		self.l_cookies = QLabel('Your cookies: ', self)
		self.l_cookies.move(50, 30)
		self.l_cookies.setFont(font)

		self.cookies = QLineEdit(self)
		self.cookies.setPlaceholderText('Enter your cookies: ')
		self.cookies.move(150, 30)

		self.l_content = QLabel('Your content: ', self)
		self.l_content.move(50, 60)
		self.l_content.setFont(font)

		self.content = QLineEdit(self)
		self.content.setPlaceholderText('Enter your cookies: ')
		self.content.move(150, 60)

		self.l_id = QLabel('Id of your friend: ', self)
		self.l_id.move(30, 90)
		self.l_id.setFont(font)

		self.id = QLineEdit(self)
		self.id.setPlaceholderText('Enter the id of your friend: ')
		self.id.move(150, 90)

		self.l_quantity = QLabel('Quantity: ', self)
		self.l_quantity.move(50, 120)
		self.l_quantity.setFont(font)

		self.quantity = QSpinBox(self)
		self.quantity.move(150, 120)
		self.quantity.setMaximum(10000)

		button = QPushButton('Post', self)
		button.move(150, 150)
		button.clicked.connect(self.post)

		self.show()

	def post(self):
		cookies = self.cookies.text()
		content = self.content.text()
		quantity = self.quantity.value()
		id_ = self.id.text()
		c_json = pa.convert_cookie_to_json(cookies)
		fb_dtsg = pa.get_fb_dtsg(c_json)
		fb.spamTimeline(content, id_, quantity, fb_dtsg, c_json)

class SendWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Send Message To Friend')
		self.setGeometry(50, 50, 400, 400)
		self.UI()

	def UI(self):
		self.l_cookies = QLabel('Your cookies: ', self)
		self.l_cookies.move(50, 30)
		self.l_cookies.setFont(font)

		self.cookies = QLineEdit(self)
		self.cookies.setPlaceholderText('Enter your cookies: ')
		self.cookies.move(150, 30)

		self.l_content = QLabel('Content: ', self)
		self.l_content.setFont(font)
		self.l_content.move(70, 60)

		self.content = QLineEdit(self)
		self.content.setPlaceholderText('Enter the content: ')
		self.content.move(150, 60)

		self.l_spinBox = QLabel('Quantity: ', self)
		self.l_spinBox.move(70, 120)
		self.l_spinBox.setFont(font)

		self.l_id = QLabel('Id of your friend: ', self)
		self.l_id.move(30, 90)
		self.l_id.setFont(font)

		self.id = QLineEdit(self)
		self.id.setPlaceholderText('Enter the id of your friend: ')
		self.id.move(150, 90)

		self.spinBox = QSpinBox(self)
		self.spinBox.move(150, 120)
		self.spinBox.setMaximum(10000)

		button = QPushButton('Send', self)
		button.move(150, 150)
		button.clicked.connect(self.send)
		self.show()

	def send(self):
		cookies = self.cookies.text()
		content = self.content.text()
		id_ = self.id.text()
		quantity = self.spinBox.value()
		c_json = pa.convert_cookie_to_json(cookies)
		fb_dtsg = pa.get_fb_dtsg(c_json)
		fb.sendMess1(id_, fb_dtsg, content, quantity, c_json)

class CommentWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Comment post')
		self.setGeometry(50, 50, 400, 400)
		self.UI()

	def UI(self):
		self.l_cookies = QLabel('Your cookies: ', self)
		self.l_cookies.move(50, 30)
		self.l_cookies.setFont(font)

		self.cookies = QLineEdit(self)
		self.cookies.setPlaceholderText('Enter your cookies: ')
		self.cookies.move(150, 30)

		self.l_content = QLabel('Content: ', self)
		self.l_content.setFont(font)
		self.l_content.move(70, 60)

		self.content = QLineEdit(self)
		self.content.setPlaceholderText('Enter the content: ')
		self.content.move(150, 60)

		self.l_link = QLabel('Link of status: ', self)
		self.l_link.move(40, 90)
		self.l_link.setFont(font)

		self.link = QLineEdit(self)
		self.link.move(150, 90)
		self.link.setPlaceholderText('Enter the link: ')

		self.l_spinBox= QLabel('Quantity: ', self)
		self.l_spinBox.setFont(font)
		self.l_spinBox.move(70, 120)

		self.spinBox = QSpinBox(self)
		self.spinBox.move(150, 120)
		self.spinBox.setMaximum(10000)

		self.button = QPushButton('Comment', self)
		self.button.clicked.connect(self.comment)
		self.button.move(150, 150)
		self.show()

	def comment(self):
		cookies = self.cookies.text()
		content = self.content.text()
		quantity = self.spinBox.value()
		link = self.link.text()
		c_json = pa.convert_cookie_to_json(cookies)
		fb_dtsg = pa.get_fb_dtsg(c_json)
		fb.commentPostFriend(content, fb_dtsg, link, quantity, c_json)



class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Tool Facebook')
		self.setGeometry(50, 50, 400, 400)
		self.UI()

	def UI(self):
		label = QLabel('Chọn 1 thôi nha pé', self)
		label.move(140, 20)
		label.setFont(font1)

		self.post = QRadioButton('Đăng bài lên trang cá nhân', self)
		self.post.move(80, 50)

		self.send = QRadioButton('Gửi tin nhắn cho bạn bè', self)
		self.send.move(80, 80)

		self.post_ = QRadioButton('Đăng bài lên trang cá nhân của bạn bè', self)
		self.post_.move(80, 110)

		self.comment = QRadioButton('Spam bình luận', self)
		self.comment.move(80, 140)


		notification = QLabel('Thông tin của thầy Thành', self)
		notification.move(120, 250)
		notification.setFont(font1)

		facebook = QLabel('Facebook của thầy: facebook.com/thanhvipvclok', self)
		facebook.move(50, 280)

		email = QLabel('Gmail của thầy: thanhmaxdz2003@gmail.com', self)
		email.move(50, 310)

		stk = QLabel('Nhớ Donate cho thầy: 0988204680 MBBank', self)
		stk.move(50, 340)

		button = QPushButton('Gét gô', self)
		button.move(160, 180)
		button.clicked.connect(self.get)
		self.show()

	def get(self):
		if self.post.isChecked():
			self.w = PostWindow()
		elif self.send.isChecked():
			self.w1 = SendWindow()
		elif self.comment.isChecked():
			self.w2 = CommentWindow()
		elif self.post_.isChecked():
			self.w3 = spamTimeline()
App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec_())