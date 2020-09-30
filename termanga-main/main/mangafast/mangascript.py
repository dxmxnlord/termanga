from getchapter import get_chapter
# from downloadpage import download_page
from searchmanga import search_manga
from getmanga import get_manga
# from showmanga import show_manga
# from deletechapter import delete_chapter

if __name__ == "__main__":
	get_chapter(get_manga(search_manga()))
	# delete_chapter()