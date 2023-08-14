import instaloader

ig = instaloader.Instaloader()

insta_page = input("Enter the name of the instagram page..: ")

ig.download_profile(insta_page, profile_pic_only=False)

