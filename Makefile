all:
	rm -rf compiled-lectures
	bundle exec thor rebuild
	cp -r compiled/lectures compiled-lectures
