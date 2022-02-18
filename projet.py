import lvgl as lv
lv.init()

import SDL
SDL.init()

# Register SDL display driver.

disp_buf1 = lv.disp_buf_t()
buf1_1 = bytearray(480*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.buffer = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 480
disp_drv.ver_res = 320
disp_drv.register()

# Regsiter SDL mouse driver

indev_drv = lv.indev_drv_t()
indev_drv.init() 
indev_drv.type = lv.INDEV_TYPE.POINTER;
indev_drv.read_cb = SDL.mouse_read;
indev_drv.register();

##### main script #####
from imagetools import get_png_info, open_png

# set dark theme :
from lv_colors import lv_colors

LV_THEME_DEFAULT_COLOR_PRIMARY=lv.color_hex(0x01a2b1)
LV_THEME_DEFAULT_COLOR_SECONDARY=lv.color_hex(0x44d1b6)

flag=lv.THEME_MATERIAL_FLAG.DARK
theme = lv.theme_material_init(LV_THEME_DEFAULT_COLOR_PRIMARY,LV_THEME_DEFAULT_COLOR_SECONDARY,flag,
                                       lv.theme_get_font_small(), lv.theme_get_font_normal(), 			
                                       lv.theme_get_font_subtitle(), lv.theme_get_font_title())

def open_img(directory, w, h):
	decoder = lv.img.decoder_create()
	decoder.info_cb = get_png_info
	decoder.open_cb = open_png
	
	f = open(directory,"rb")
	img_data = f.read()

	data = lv.img_dsc_t(
	    {
		"data": img_data,
		"data_size": len(img_data)
	    }
	)
	return data


def create_btn(cont, directory, align, w, h, x, y):
	style=lv.style_t()
	style.init()
	style.set_image_recolor_opa(lv.STATE.PRESSED, lv.OPA._30)
	style.set_image_recolor(lv.STATE.PRESSED, lv_colors.BLACK)
	
	button = lv.imgbtn(cont, None)
	button.set_src(lv.btn.STATE.RELEASED, open_img(directory, w, h))
	button.set_src(lv.btn.STATE.PRESSED, open_img(directory, w, h))
	button.set_checkable(True)
	button.add_style(lv.imgbtn.PART.MAIN, style)
	button.align(None, align, x, y)
	button.set_size(w, h)
	
	return button

def goBack(source, evt):
	if evt == lv.EVENT.CLICKED :
		if source == dm_back :
			lv.scr_load_anim(home_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
		if source == music_back :
			lv.scr_load_anim(home_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
		if source == BT_back :
			lv.scr_load_anim(home_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
		if source == stat_back :
			lv.scr_load_anim(home_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
		if source == nav_back :
			lv.scr_load_anim(home_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
		if source == radio_back :
			lv.scr_load_anim(home_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
           
def goScr(source, evt):
	if evt == lv.EVENT.CLICKED:
		if source == dm_btn :
			lv.scr_load_anim(DM_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
		if source == music_btn:
			lv.scr_load_anim(music_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
		if source == stat_btn:
			lv.scr_load_anim(stat_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
			crate_page(flevel, name, roller)
		if source == nav_btn:
			lv.scr_load_anim(nav_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)
		if source == BT_btn: 
			lv.scr_load_anim(BT_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)	   	
		if source == radio_btn:
			lv.scr_load_anim(radio_scr,lv.SCR_LOAD_ANIM.FADE_ON,500,10,False)

style=lv.style_t()
style.init()
style.set_image_recolor_opa(lv.STATE.PRESSED, lv.OPA._30)
style.set_image_recolor(lv.STATE.PRESSED, lv_colors.BLACK)

#########################################################
#####################Home screen#########################
#########################################################

music_scr=lv.obj(None,None)
DM_scr=lv.obj(None,None)
radio_scr=lv.obj(None,None)
nav_scr=lv.obj(None,None)
stat_scr=lv.obj(None,None)
BT_scr=lv.obj(None,None)
home_scr = lv.scr_act()


lv.img.cache_set_size(4)

dm_btn = create_btn(lv.scr_act(),"driving.png", lv.ALIGN.CENTER, 130, 130, -155, -75) #driving mode
dm_btn.set_event_cb(goScr)

radio_btn = create_btn(lv.scr_act(),"radio.png",lv.ALIGN.CENTER, 130, 130, 0, -75)   #radio
radio_btn.set_event_cb(goScr)

BT_btn = create_btn(lv.scr_act(),"BT.png",lv.ALIGN.CENTER, 130, 130, 155, -75)       #bluetooth
BT_btn.set_event_cb(goScr)

nav_btn = create_btn(lv.scr_act(),"nav.png",lv.ALIGN.CENTER, 130, 130, -155, 75)
nav_btn.set_event_cb(goScr)

music_btn = create_btn(lv.scr_act(),"music.png",lv.ALIGN.CENTER, 130, 130, 0, 75)
music_btn.set_event_cb(goScr)

stat_btn = create_btn(lv.scr_act(),"status.png",lv.ALIGN.CENTER, 130, 130, 155, 75)
stat_btn.set_event_cb(goScr)

#####################################
###############Music#################
#####################################

music_label = lv.label(music_scr,None)
music_label.set_text("MUSIC")
music_label.align(None, lv.ALIGN.IN_TOP_MID, 0, 15)

trk = 1
def music_handler(source, evt):
	global trk
	title = "TRACK "
	volume = vol.get_value()
	if evt == lv.EVENT.CLICKED:
		if source == vol_up :
			volume += 10
			if volume >= 100 :
				volume = 100
			vol.set_value(volume, False)
		if source == vol_down :
			volume -= 10
			if volume <= 0 :
				volume = 0
			vol.set_value(volume, False)
		if source == next_btn :
			track.set_value(0, False)
			trk += 1
			title += str(trk)
			track_label.set_text(title)
			if trk >= 20 :
				trk = 0
		if source == prev_btn :
			track.set_value(0, False)
			trk -= 1
			if trk == 0 :
				trk = 1
			title += str(trk)
			track_label.set_text(title)
			

PP_btn = lv.imgbtn(music_scr, None)
PP_btn.set_src(lv.btn.STATE.RELEASED, open_img("play.png", 80, 80))
PP_btn.set_src(lv.btn.STATE.PRESSED, open_img("play.png", 80, 80))
PP_btn.set_src(lv.btn.STATE.CHECKED_RELEASED, open_img("pause.png", 80, 100))
PP_btn.set_src(lv.btn.STATE.CHECKED_PRESSED, open_img("pause.png", 80, 100))
PP_btn.set_checkable(True)
PP_btn.add_style(lv.imgbtn.PART.MAIN, style)
PP_btn.align(None, lv.ALIGN.IN_TOP_LEFT, 150, 180)

music_back = create_btn(music_scr, "goback.png",lv.ALIGN.CENTER, 50, 50, -210, -120)
music_back.set_event_cb(goBack)

vol = lv.slider(music_scr,None)
vol.set_width(15)
vol.set_height(150)
vol.align(None,lv.ALIGN.CENTER,200,0)
vol.set_range(0, 100)

next_btn = create_btn(music_scr, "next.png",lv.ALIGN.IN_TOP_LEFT, 50, 50, 240, 195)
next_btn.set_event_cb(music_handler)

prev_btn = create_btn(music_scr, "prev.png",lv.ALIGN.IN_TOP_LEFT, 50, 50, 90, 195)
prev_btn.set_event_cb(music_handler)

vol_up = create_btn(music_scr, "plus.png", lv.ALIGN.CENTER, 40, 40, 200, -115)
vol_up.set_event_cb(music_handler)

vol_down = create_btn(music_scr, "minus.png", lv.ALIGN.CENTER, 40, 40, 200, 115)
vol_down.set_event_cb(music_handler)

track = lv.slider(music_scr,None)
track.set_width(250)
track.set_height(15)
track.align(None,lv.ALIGN.IN_TOP_LEFT,60,150)
track.set_range(0, 330)

track_label = lv.label(music_scr,None)
track_label.set_text("TRACK 1")
track_label.set_width(50)
track_label.align(None, lv.ALIGN.CENTER, -50, -35)

############################################
###############driving mode#################
############################################

DM_label = lv.label(DM_scr,None)
DM_label.set_text("DRIVING MODE")
DM_label.align(None, lv.ALIGN.IN_TOP_MID, 0, 15)

dm_back = create_btn(DM_scr, "goback.png",lv.ALIGN.CENTER, 50, 50, -210, -120)
dm_back.set_event_cb(goBack)

def mbox_handler(obj, event):
    if event == lv.EVENT.VALUE_CHANGED:
        mbox1.del_async()

val = 0
inc = 2
flevel = 200

def gauge_anim(gauge,val):
    gauge.set_value(0,val)

def gauge_handler(source,evt):
	global val, inc, flevel, mbox1
	if evt == lv.EVENT.VALUE_CHANGED:
		mode = roller.get_selected()
		if mode == 0 :
			inc = 2
			needle_colors=lv_colors.GREEN
			gauge1.set_needle_count(1, needle_colors)
		if mode == 1:
			inc = 4
			needle_colors=lv_colors.BLUE
			gauge1.set_needle_count(1, needle_colors)
		if mode == 2:
			inc = 6
			needle_colors=lv_colors.RED
			gauge1.set_needle_count(1, needle_colors)	
	if evt == lv.EVENT.PRESSING:
		if source == Accelerate:
			if flevel > 0 :
				val = gauge1.get_value(0)
				val += inc
				flevel -= int(inc/2)
				if flevel <= 0 :
					flevel = 0
					btns = ["Close", ""]
					mbox1 = lv.msgbox(DM_scr)
					mbox1.set_text("Empty fuel tank ! Please refill at the nearest station.")
					mbox1.add_btns(btns)
					mbox1.set_width(200)
					mbox1.set_event_cb(mbox_handler)
					mbox1.align(None, lv.ALIGN.CENTER, 0, 0)
				if val > 300 :
					val = 290
				gauge1.set_value(0, val)
				fuel.set_value(flevel)
		        
	if evt == lv.EVENT.RELEASED :
		if source == Accelerate:
			a_ga=lv.anim_t()
			a_ga.init()
			a_ga.set_values(val, 0)
			a_ga.set_time(1000)
			a_ga.set_custom_exec_cb(lambda a, val: gauge_anim(gauge1,val))
			lv.anim_t.start(a_ga)
			val = gauge1.get_value(0)
            
Accelerate = lv.btn(DM_scr,None)
Accelerate.set_event_cb(gauge_handler)
Accelerate.align(None,lv.ALIGN.IN_TOP_LEFT,65,260)
Accelerate_label=lv.label(Accelerate,None)
Accelerate_label.set_text("Accelerate")

needle_colors=lv_colors.BLUE

gauge1=lv.gauge(DM_scr,None)
gauge1.set_range(0, 300)
gauge1.set_critical_value(280)
gauge1.set_needle_count(1, needle_colors)
gauge1.set_size(200,200)
gauge1.align(None,lv.ALIGN.CENTER,-110,-20)

roller = lv.roller(DM_scr,None)
roller.set_options("ECO Mode\n"
                   "NORMAL Mode\n"
                   "SPORT Mode",
                   lv.roller.MODE.INFINITE)
roller.set_visible_row_count(3)
roller.align(None,lv.ALIGN.CENTER,100,80) 
roller.set_event_cb(gauge_handler)


fuel = lv.arc(DM_scr,None)
fuel.set_end_angle(200)
fuel.set_size(140,140)
fuel.set_range(0,200)
fuel.align(None,lv.ALIGN.CENTER,100,-50)
fuel.set_value(flevel)

#####################################
###############radio#################
#####################################

stations = [["Shems FM", "88.7"],
			["Express FM", "95.2"],   
			["IFM", "100.6"], 
			["Jawhara FM", "102.5"],
			["Mosaique FM", "105.8"]]

"""
def get_index(val, l):
	return min(range(len(l)), key=lambda i: abs(float(l[i][1])-val))"""

idx = 0
def radio_handler(source, evt):
	global idx
	global stations
	if evt == lv.EVENT.CLICKED:
		if source == next_stn :
			station.set_text(stations[idx][0])
			stn_freq.set_text(stations[idx][1] + " MHZ")
			freq.set_value(round(float(stations[idx][1])), False)
			idx += 1
			if idx > (len(stations)-1) :
				idx = 0
		if source == prev_stn :
			station.set_text(stations[idx][0])
			stn_freq.set_text(stations[idx][1] + " MHZ")
			freq.set_value(round(float(stations[idx][1])), False)
			idx -= 1
			if idx < 0 :
				idx = (len(stations)-1)

RADIO_label = lv.label(radio_scr,None)
RADIO_label.set_text("RADIO")
RADIO_label.align(None, lv.ALIGN.IN_TOP_MID, 0, 15)

radio_back = create_btn(radio_scr, "goback.png",lv.ALIGN.CENTER, 50, 50, -210, -120)
radio_back.set_event_cb(goBack)

freq = lv.slider(radio_scr,None)
freq.set_width(350)
freq.set_height(10)
freq.align(None,lv.ALIGN.CENTER,0 ,50)
freq.set_range(87, 110)

station = lv.label(radio_scr,None)
station.set_text("Please choose a station")
station.align(None, lv.ALIGN.CENTER, 0, -35)

stn_freq = lv.label(radio_scr,None)
stn_freq.set_text("00.0 MHZ")
stn_freq.align(None, lv.ALIGN.CENTER, 0, 5)

next_stn = create_btn(radio_scr,"next_stn.png",lv.ALIGN.CENTER, 40, 40, 65, 5)
next_stn.set_event_cb(radio_handler)

prev_stn = create_btn(radio_scr,"prev_stn.png",lv.ALIGN.CENTER, 40, 40, -65, 5)
prev_stn.set_event_cb(radio_handler)

##########################################
###############navigation#################
##########################################

nav_label = lv.label(nav_scr,None)
nav_label.set_text("NAVIGATION")
nav_label.align(None, lv.ALIGN.IN_TOP_MID, 0, 15)

nav_back = create_btn(nav_scr, "goback.png",lv.ALIGN.CENTER, 50, 50, -210, -120)
nav_back.set_event_cb(goBack)

prompt = lv.img(nav_scr, None)
prompt.set_src(open_img("nav_prb.png", 250, 250))
prompt.align(nav_scr, lv.ALIGN.CENTER, -90, 15)

prompt_label = lv.label(nav_scr, None)
prompt_label.set_width(100)
prompt_label.set_text("An Error has occured !!\nIt seems that no GPS \nmodule has been detected.\nPlease contact your car \ndealer for more details.")
prompt_label.align(None, lv.ALIGN.CENTER, 130, 0)

#########################################
###############Bluetooth#################
#########################################

BT_label = lv.label(BT_scr,None)
BT_label.set_text("BLUETOOTH")
BT_label.align(None, lv.ALIGN.IN_TOP_MID, 0, 15)

BT_back = create_btn(BT_scr, "goback.png",lv.ALIGN.CENTER, 50, 50, -210, -120)
BT_back.set_event_cb(goBack)

name = ""
def BT_handler(obj, event):
	global mbox1, name
	list_btn = lv.list.__cast__(obj)
	if event == lv.EVENT.CLICKED:
		name = list_btn.get_btn_text()
		btns = ["Close", ""]
		mbox1 = lv.msgbox(BT_scr)
		mbox1.set_text("You are now connected to : "+ name)
		mbox1.add_btns(btns)
		mbox1.set_width(180)
		mbox1.set_event_cb(mbox_handler)
		mbox1.align(None, lv.ALIGN.CENTER, 0, 0)
		
list1 = lv.list(BT_scr)
list1.set_size(200, 200)
list1.align(None, lv.ALIGN.CENTER, 0, 0)

for i in range(1, 16):
	list_btn = list1.add_btn(lv.SYMBOL.DUMMY, "Device "+str(i))
	list_btn.set_event_cb(BT_handler)

######################################
###############status#################
######################################

stat_label = lv.label(stat_scr,None)
stat_label.set_text("STATUS")
stat_label.align(None, lv.ALIGN.IN_TOP_MID, 0, 15)

stat_back = create_btn(stat_scr, "goback.png",lv.ALIGN.CENTER, 50, 50, -210, -120)
stat_back.set_event_cb(goBack)

def stat(flevel, name, roller):
	stat_txt = "Car name : Chiheb's car\nCar model : Vxxxx SIxxx\nSerial Number : 2407CN1999\nNumber Plate : 1877 TN 202\nInfotainment system version : 1.03\nFuel Level : " + str(flevel / 2)[0:4] + ' %\n'
	buff=" "*13
	roller.get_selected_str(buff,len(buff))
	#stat_txt += ("Current Driving Mode : " + buff+"\n")
	if name == "" :
		stat_txt += "Current device connected to BlueTooth : None\n"
	else : stat_txt = stat_txt + "Current device connected to BlueTooth : "+name+"\n"
	stat_txt += "Current speed : 0 KM/H\nCar Errors : \n   -No GPS module detected\n"
	if flevel <= 20 :
		stat_txt +="   -Low fuel level\n"
	return stat_txt

def crate_page(flevel, name, roller):

	page = lv.page(stat_scr,None)
	page.set_size(360,240)
	page.align(None,lv.ALIGN.CENTER,0,0)

	label = lv.label(page, None);
	label.set_long_mode(lv.label.LONG.BREAK);            
	label.set_width(lv.page.get_width_fit(page))        
	label.set_text(stat(flevel, name, roller))




