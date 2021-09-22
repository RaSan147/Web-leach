# pylint: disable=anomalous-backslash-in-string
import mimetypes
# for testing
Project = main_link = link_startswith = file_types = file_starts = sub_dirs = sp_flags= sp_extension = overwrite_bool = dimention = dl_done = sequence = sub_links = has_missing = dir_sorted = 0

class Constants:
	"""Stores most commonly used constants
	"""

	# file types
	all_image_types = "3FR 3G2 3GP ARW AVI CANVAS CAPTION CR2 CR3 CRW CUBE CUT DCM DCR DCRAW DFONT DNG EMF ERF FILE FRACTAL FTP GRADIENT HALD HEIC HEIF HTTP HTTPS IIQ JNX K25 KDC LABEL MAC MEF MRW NEF NRW ORA ORF OTF PANGO PATTERN PEF PES PFA PFB PIX PLASMA PWP RADIAL-GRADIENT RAF RAW RGB565 RLA RLE RMF RW2 SCR SCREENSHOT SCT SFW SR2 SRF STEGANO TEXT TILE TIM TM2 TTC TTF WMF WPG X3F XC XCF XPS JPG PNG TIFF GIF WEBP BMP EPS PDF APNG A AAI AI ART AVIF AVS B BGR BGRA BGRO BMP2 BMP3 C CAL CALS CIN CLIP CLIPBOARD CMYK CMYKA CUR DATA DCX DDS DPX DXT1 DXT5 EPDF EPI EPSF EPSI EPT EPT2 EPT3 EXR FARBFELD FAX FF FITS FL32 FLIF FLV FTS G G3 G4 GIF87 GRAY GRAYA GROUP4 HDR HRZ ICB ICO ICON INLINE IPL J2C J2K JNG JP2 JPC JPE JPEG JPM JPS JPT JXL K M M2V M4V MAP MASK MAT MIFF MKV MNG MONO MOV MP4 MPC MPEG MPG MSL MSVG MTV MVG NULL O OTB PAL PALM PAM PBM PCD PCDS PCL PCT PCX PDB PDFA PFM PGM PGX PHM PICON PICT PJPEG PNG00 PNG24 PNG32 PNG48 PNG64 PNG8 PNM POCKETMOD PPM PS PSB PSD PTIF R RAS RGB RGBA RGBO RGF RSVG SGI SIX SIXEL SUN SVG SVGZ TGA TIFF64 TXT UYVY VDA VICAR VID VIFF VIPS VST WBMP WEBM WMV XBM XPM XV Y YCbCr YCbCrA YUV ASHLAR BRF CIP EPS2 EPS3 HISTOGRAM HTM HTML INFO ISOBRL ISOBRL6 JSON MATTE PS2 PS3 SHTML SPARSE-COLOR THUMBNAIL UBRL UBRL6 UIL YAML A AAI APNG ASHLAR AVIF AVS B BGR BGRA BGRO C CLIP CMYK CMYKA DATA DCX DDS DXT1 DXT5 EPS3 EPT3 FAX FLIF FLV G GIF GRAY GRAYA HDR ICO INFO INLINE IPL JSON K M M2V M4V MASK MAT MATTE MIFF MKV MNG MOV MP4 MPC MPEG MPG MSL MSVG MTV O PALM PAM PBM PCL PDB PDF PDFA PFM PGM PHM PNM POCKETMOD PPM PS PS2 PS3 PSB PSD PTIF R RAS RGB RGBA RGBO RSVG SGI SPARSE-COLOR SUN SVG SVGZ THUMBNAIL TIFF TIFF64 TXT VID VIFF VIPS WEBM WEBP WMV XV Y YAML YCbCr YCbCrA".lower().split()
	all_video_types = "webm mkv flv vob ogv ogg drc gif apng gifv mng avi mts m2ts ts mov qt wmv yuv rm rmvb viv ask amv mp4 m4p m4v mpg mp2 mpeg mpe mpv m2v 3gp 3g2 mxf roq nsv flv f4v f4p f4a f4b asf wmv avi divx evo avi mkv mk3d m2p ps mpg m2ts mxf ogg ogv ogx mov qt vob mpa mpe mpv2 lsf lsx asf asr asxavi movie".lower().split()
	all_audio_types = "3gp aa aac aax act aiff alac amr ape au awb dss dvf flac gsm iklax ivs m4 m4b m4p mmf mp3 mpc msv nmf ogg oga mogg opus ra rm raw rf64 sln tta voc vox wav wma wvwebm 8svx cda snd mid rmi aif aifc m3u ra ram".lower().split()

	# DLC links
	who_r_u = 'https://www.myinstants.com/media/sounds/who_r_u_1.mp3'
	yamatte = ('https://www.myinstants.com/media/sounds/yamatte.mp3', 'https://www.myinstants.com/media/sounds/ara-ara.mp3', 'https://www.myinstants.com/media/sounds/ara-ara2.mp3')

	# conversation words
	yes = ('y', 'yes', 'yeah', 'sure', 'ok', 'lets go', "let's go", 'start', 'yep', 'yep', 'well y', 'well yes', 'well yeah', 'well sure', 'well ok', 'well lets go', "well let's go", 'well start', 'well yep', 'well yep', 'actually y', 'actually yes', 'actually yeah', 'actually sure', 'actually ok', 'actually lets go', "actually let's go", 'actually start', 'actually yep', 'actually yep')
	no = ('n', 'no', 'na', 'nah', 'nope', 'stop', 'quit', 'exit', 'not really', 'no', 'not at all', 'never', 'well n', 'well no', 'well na', 'well nah', 'well nope', 'well stop', 'well quit', 'well exit', 'well not really', 'well no', 'well not at all', 'well never', 'actually n', 'actually no', 'actually na', 'actually nah', 'actually nope', 'actually stop', 'actually quit', 'actually exit', 'actually not really', 'actually no', 'actually not at all', 'actually never')
	cond = yes + no
	condERR = "/y/Sorry,  I can't understand what you are saying./=/\n Just type yes or no.   "
	hard_cancel = '/y/Hand Cancel Command entered.\nExiting.../=/'

	special_starts = {'nh':'https://nhentai\.((net)|(to)|(xxx))/g/',
		'mangafreak':'https://w[^\/]+\.mangafreak.net/(?:M|m)anga/([^\?\#]+)',
		'nh_sc':'^nh (\d+)$',
		'mf_sc':'^mf (.+)$',
		'pinterest':'https://www.pinterest.com/',
		'mf_read':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(?:_\d+)[\?\#]?.*',
		'mf_read_chap':'https:\/\/w[\d]+\.mangafreak\.net\/Read1_([^\?\#]+)(_\d+)[\?\#]?.*',
		'webtoon_ep':'https\:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/.*?\/viewer\?title_no\=(\d+)\&episode_no\=\d+',
		'webtoon': 'https:\/\/www\.webtoons\.com\/en\/(.*?)\/(.*?)\/list\?title_no=(\d+)'}

	extensions_map = mimetypes.types_map.copy()
	extensions_map.update({
		'': 'application/octet-stream', # Default
		'.py': 'text/plain',
		'.c': 'text/plain',
		'.h': 'text/plain',
		})

	old_img = ('jpeg', 'jpg', 'png', 'gif', 'webp', 'bmp', 'tif')

	DEFAULT_DISABLE_LIB_CHECK = True # temporarily disabled

true = True
false = False
none = None


def leach_logger(*args):
	pass

def log(arr):
	for i in range(len(arr)):
		if type(arr) is str:
			continue
		if type(arr[i]) is bytes:
			arr[i] = arr[i].decode('utf-8')
		else:
			arr[i] = str(arr[i])

	return "||".join(map(str, arr))




