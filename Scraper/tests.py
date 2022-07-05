from turtle import title
from django.test import TestCase

# Create your tests here.
class ArticleTestCase(TestCase):
    def SetUp(self):
        title = "Windows 11 update copies popular Android feature - and we couldn't be happier"
        desc =  "box for Windows 11, letting you open files in a different app to the one you've set as default."
        img =   "https://cdn.mos.cms.futurecdn.net/AJipb6S4wzdwPdw9AGJ7wk-1024-80.png.webp"
        ur = "https://lithub.com/the-language-of-loneliness-five-books-that-reckon-with-not-belonging/?fbclid=IwAR1aQ7wShWLi2ckS_2YngHN_B6HtsQC_MOFiPkuVuoh5YYlW_0Hdvq-n3hY"
    def test_article_content(self):
        self.assertEqual(title, "Windows 11 update copies popular Android feature - and we couldn't be happier")
        self.assertEqual(desc, "Windows 11 update copies popular Android feature - and we couldn't be happier")
        self.assertEqual(img, "https://cdn.mos.cms.futurecdn.net/AJipb6S4wzdwPdw9AGJ7wk-1024-80.png.webp")
        self.assertEqual(ur, "https://lithub.com/the-language-of-loneliness-five-books-that-reckon-with-not-belonging/?fbclid=IwAR1aQ7wShWLi2ckS_2YngHN_B6HtsQC_MOFiPkuVuoh5YYlW_0Hdvq-n3hY")
