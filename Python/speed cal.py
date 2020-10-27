from speedtest import speedtest #pip install
	st=speedtest()
	print("your connection Download speed",st.download())
	print("Your connection upload speed ",st.upload())