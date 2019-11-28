default:
	@echo "setting up..."
	@touch user.txt; \
	echo $(shell whoami) >> "user.txt"

install: 
	@echo "installing termanga..."
	@echo "copying files to appropriate directories..."
	@export user=$(shell cat user.txt); \
	mkdir /home/$${user}/Termanga/; \
	cp -rp ./termanga-main/* /home/$${user}/Termanga/; \
	chmod +x /home/$${user}/Termanga/main/app/*; \
	touch termanga.sh; \
	echo "#!/bin/bash" >> termanga.sh; \
	echo "cd /home/$${user}/Termanga/main/app/" >> termanga.sh; \
	echo "./menu.sh" >> termanga.sh; \
	chmod 777 termanga.sh; \
	sudo cp termanga.sh /usr/bin/; \
	sudo mv /usr/bin/termanga.sh /usr/bin/termanga; \
	echo "finishing up...";
	@cd ..; \
	rm -fr termanga

uninstall: 
	@echo "removing termanga..."
	@sudo rm /usr/bin/termanga
	@export user=$(shell cat user.txt); \
	rm -fr /home/$${user}/Termanga/
	@cd ..; \
	rm -fr termanga
