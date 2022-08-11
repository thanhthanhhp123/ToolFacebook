import requests
from bs4 import BeautifulSoup as BS
from time import sleep as sl

def sendMess1(idSend,fb_dtsg,content,quantity,cookies):
	url = "https://mbasic.facebook.com/messages/send/?icm=1&refid=12"
	data = {
		'fb_dtsg': fb_dtsg,
		'body': content,
		'wwwupp': 'C3',
		'ids['+idSend+']': idSend,
		'referrer': '',
		'ctype': '',
		'cver': 'legacy'
	}
	for i in range(quantity):
		requests.post(url,cookies = cookies,data = data)
		

def commentPostFriend(content,fb_dtsg,link_status,quantity,cookies):
	url = "https://m.facebook.com/a/comment.php?fs=8&actionsource=2&comment_logging&ft_ent_identifier="+link_status
	for i in range(quantity):
		data = {
		'fb_dtsg': fb_dtsg,
		'comment_text': content,
		'privacy_value': '0',
		'conversation_guide_session_id': 'null',
		'conversation_guide_shown': 'none',
		'waterfall_source': 'photo_comment',
		'submit': 'Đăng',
		}
		requests.post(url,cookies = cookies,data = data)
		sl(1)

def spamTimeline(content,ids,quantity,fb_dtsg,cookies):
	url = "https://m.facebook.com/a/wall.php?id="+ids
	s="."
	for i in range(quantity):
		s+="."
		data = {
		'fb_dtsg': fb_dtsg,
		'jazoest': '21843',
		'target': ids,
		'message': content+s
		}
		requests.post(url,cookies =cookies,data = data)
		sl(1)

def autoPostStatus(content,quantity,fb_dtsg,cookies):
	myID = cookies['c_user']
	url = "https://m.facebook.com/composer/mbasic/?av="+myID
	s = "."
	for i in range(quantity):
		s += "."
		data = {
		'fb_dtsg': fb_dtsg,
		'privacyx': '300645083384735',
		'target': myID,
		'c_src': 'feed',
		'referrer': 'feed',
		'xc_message': content+s,
		'view_post': 'Đăng',
		}
		requests.post(url,cookies =cookies,data = data)
		sl(1)

def changePrivacy(myID,idPost,choice,fb_dtsg,cookies):
	idPost = idPost.split("_")[1]
	post = 'privacy_scope_renderer:{"id":'+idPost+'}'
	post = post.encode("ascii")
	post = base64.b64encode(post).decode("utf-8")
	privacy = ""
	if choice == "public":
		privacy = "EVERYONE"
	elif choice == "friend":
		privacy = "FRIENDS"
	elif choice == "notpublic":
		privacy = "SELF"
	variables='{"input":{"privacy_mutation_token":null,"privacy_row_input":{"allow":[],"base_state":"'+privacy+'","deny":[],"tag_expansion_state":"UNSPECIFIED"},"privacy_write_id":"'+post+'","render_location":"COMET_STREAM","actor_id":"'+myID+'","client_mutation_id":"3"},"privacySelectorRenderLocation":"COMET_STREAM","scale":1,"storyRenderLocation":"timeline","tags":null}'
	url = "https://www.facebook.com/api/graphql/"
	data = {
		'fb_dtsg': fb_dtsg,
		'doc_id': '4879007762150284',
		'variables': variables
	}
	requests.post(url,cookies=cookies,data=data)
	sl(2)