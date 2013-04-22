all:
	rm -rf compiled-lectures
	bundle exec thor rebuild
	cp -rf compiled/* ../../lectures/
