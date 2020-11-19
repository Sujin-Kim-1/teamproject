from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='products', null=True)
    created_at = models.DateTimeField()


    #여기서부터 추가함
    GENDER = ( (1, '여성'), (2, '남성') )
    gender = models.CharField(max_length=2, choices=GENDER)

    PRODUCTTYPE = ( (1, '관심상품'), (2, '보유상품'))
    producttype = models.CharField(max_length=2, choices=TYPE)
    
    CATEGORY_M = ((1, '아우터'), (2, '상의'), (2, '바지'))
    category_m = models.CharField(max_length=3, choices=CATEGORY_M)

    CATEGORY_W = ((1, '아우터'), (2, '상의'), (3, '바지'), (4, '스커트'), (5, '원피스'))   
    category_w = models.CharField(max_length=5, choices=CATEGORY_W)

    CATEGORY_M_OUTER = ((1, '코트'), (2, '패딩'), (3, '자켓'), (4, '점퍼'))
    category_m_outer = models.CharField(max_length=4, choices=CATEGORY_M_OUTER)

    CATEGORY_M_TOP = ((1, '티셔츠'), (2, '셔츠'), (3, '니트'), (4, '맨투맨/후드'))
    category_m_top = models.CharField(max_length=4, choices=CATEGORY_M_TOP)
    
    CATEGORY_M_PANTS = ((1, '청바지'), (2, '팬츠/슬랙스'), (3, '반바지'), (4, '트레이닝'))
    category_m_pants = models.CharField(max_length=4, choices=CATEGORY_M_PANTS)

    
    STYLE_M = ((1, '스포츠'), (2, '캐주얼'), (3, '정장/포멀'), (4, '스트릿'), (5, '빈티지'))
    style_m = models.CharField(max_length=5, choices=STYLE_M)

    COLOR = ((1, '블랙'),(2, '화이트'), (3, '그레이'), (4, '브라운'), (5, '블루'))
    color = models.CharField(max_length=5, choices=COLOR)

    SEASON= ((1, '봄'), (2, '여름'), (3, '가을'), (4, '겨울'))
    season = models.CharField(max_length=4, choices=SEASON)

    brand = models.TextField()
    productname = models.TextField()
    price = models.TextField()
    site = models.TextField()

    RATING = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rating = models.CharField(max_length=5, choices=RATING)
    
    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
            
        return f'{self.body}'
