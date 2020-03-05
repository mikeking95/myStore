# myStore
An ecommerce Store Project built with Docker, PostgreSQL and Django 2.2.
Built with guidance from "Django for Professionals" by William S Vincent.

2nd time working through the book, taking the base project from the book and extending it further to build
on my Django knowledge and experience.


  !!!!!!!!!    TODO    !!!!!!!!!!!!
  update all dependencies in Pipfile with current versions (avoid future mismatch)

Goals, Learning targets:
  - Objective: Gain confidence writing tests - Test all the Things!!
  - Objective: Implement Product Attributes for Front-End Search ( Robust search/filter functionality )
  - Objective: Make it Pretty! Start with MDB E-Commerce Templates and hook up all functionality to Django
  - Attempt: Write my own CSS / Pages

    Added, 03-03-20
  - Objective: Performance Enhancements ( as needed )
    ** Bottlenecks will reveal themselves in production. Don't fix problems you dont have ;D
     - Implement Amazon S3 Bucket for images (media)
     - CDN (s3) for static assets
     Third Party modules worth exploring further:
       - django-storages (CDN/s3)
       - django-admin-honeypot for production
       - *django-two-factor-auth : Maybe
       - easy-thumnails* (multiple image sizes)
       - django-compressor
       - django-extensions (This+9000)
       - check Google's PageSpeed Insights
