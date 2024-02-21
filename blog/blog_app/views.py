from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

all_posts = [
    {
        "slug": "real-estate-investment",
        "image": 'real_estate.jpg',
        "author": 'Michael H.',
        'date': date(2023, 10, 1),
        'title': 'Investing In Real Estate',
        'excerpt': 'Investing in real estate presents a compelling opportunity for individuals seeking to build wealth and diversify their investment portfolios',
        'content': '''
            Investing in real estate presents a compelling opportunity for individuals seeking to build wealth and diversify their investment portfolios. Unlike traditional investments such as stocks and bonds, real estate offers the unique advantage of providing a tangible asset with the potential for both rental income and long-term appreciation. Whether investing in residential properties, commercial buildings, or vacation rentals, real estate allows investors to generate passive income streams while simultaneously benefiting from property value appreciation over time. Furthermore, real estate investments offer a level of control and autonomy not found in other asset classes, empowering investors to make strategic decisions regarding property management, renovations, and rental pricing to maximize returns.
            
            One of the key advantages of real estate investment is its ability to serve as a hedge against inflation and market volatility. Real estate assets have historically demonstrated resilience during economic downturns, providing investors with a stable source of income even in challenging market conditions. Additionally, real estate investments offer tax benefits such as depreciation deductions, mortgage interest deductions, and the ability to defer capital gains taxes through 1031 exchanges. These tax advantages can significantly enhance the overall return on investment and provide investors with additional cash flow to reinvest in their portfolios or allocate towards other financial goals.

            Moreover, real estate investment allows for leveraging the power of other people's money through mortgage financing. With relatively low down payments and favorable interest rates, investors can acquire properties worth significantly more than their initial investment capital. This leverage amplifies returns on investment and accelerates wealth accumulation over time. Additionally, real estate investments provide a level of diversification to an investment portfolio, reducing overall risk and increasing stability. By spreading investment capital across different property types and geographic locations, investors can minimize exposure to market fluctuations and potentially achieve higher risk-adjusted returns. Overall, investing in real estate offers a multifaceted approach to building wealth, providing investors with a tangible asset, passive income, tax advantages, leverage, and diversification benefits.
        '''
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Michael H.",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "nature.jpg",
        "author": "Michael H.",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
]


def getPostDate(post):
    return post['date']


def index(request):
    sortedPost = sorted(all_posts, key=getPostDate)
    getLatestPost = sortedPost[-3:]
    return render(request, "blog_app/index.html", {'latest_posts': getLatestPost})


def posts(request):
    return render(request, "blog_app/posts.html", {'all_posts': all_posts})


def specificPost(request, slug):
    correct_post = next(
        post for post in all_posts if post['slug'] == slug)

    return render(request, "blog_app/specific_post.html", {'specific_post': correct_post})
