from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'name': 'Praveenkumar B',
        'role': 'Sr. Software Development Engineer',
        'social_media': {
            'instagram': 'https://www.instagram.com/itspkhere_/',
            'linkedin': 'https://www.linkedin.com/in/itspraveenkumar1152/',
            'mail': 'mailto:itspraveenkumar1152@gmail.com'
        },
        'address': '738, T K Kottay, Panaimadal, Salem - 636117',
        'description': 'Innovative Software Engineer offering 3 years of solid experience in agile software development with strong CS background.',
        'birthday': '30 June 1998',
        'age': 24,
        'website': 'https://findpk.github.io/',
        'degree': 'BE Computer Science and Engineering',
        'phone': '+91 9626166481',
        'email': 'itspraveenkumar1152@gmail.com',
        'city': 'Salem, Tamilnadu, India',
        'education': [
            {
                'course': 'BACHELOR OF ENGINEERING - COMPUTER SCIENCE & ENGINEERING',
                'institution': 'College of Engineering, Guindy, Anna University, Chennai',
                'remarks': 'CGPA - 8.65/10',
                'period': '2015 - 2019'
            },
            {
                'course': 'HSC',
                'institution': 'Sree Gokulam Matric Higher Secondary School, Valappadi, Salem',
                'remarks': 'With 96%',
                'period': '2014 - 2015'
            },
            {
                'course': 'SSLC',
                'institution': 'Govt Higher Secondary School, Panaimadal, Salem',
                'remarks': 'With 95.4%',
                'period': '2012 - 2013'
            }
        ],
        'courses': [
            {
                'course': 'Microservices Software Architecture: Patterns and Techniques',
                'provider': 'Udemy'
            },
            {
                'course': 'SOLID Principles: Introducing Software Architecture & Design',
                'provider': 'Udemy'
            },
            {
                'course': 'Agile Software Development',
                'provider': 'LinkedIn'
            },
            {
                'course': 'Domain Driven Design - Complete Software Architecture',
                'provider': 'Udemy'
            },
            {
                'course': 'Software Architexture foundatons',
                'provider': 'LinkedIn'
            },
            {
                'course': 'Modern database and application design with MongoDB',
                'provider': 'LinkedIn'
            },
            {
                'course': 'Unit testing and Test driven development',
                'provider': 'Udemy'
            },
            {
                'course': 'Advanced SQL for Query Tuning and Performance OptimizationAdvanced SQL for Query Tuning and Performance Optimization',
                'provider': 'LinkedIn'
            },
            {
                'course': 'Learning Django',
                'provider': 'LinkedIn'
            }
        ],
        'skills': [
            "C, C++, HTML, C++",
            "OOP, Data Structures",
            "Javascript, Nodejs",
            "Vue.js, React.js",
            "Python, Django",
            "Java",
            "Micro Services",
            "Agile Methodologies",
            "TDD, BDD, DDD",
            "RestAPI, Rest Assured",
            "SQL, PostgreSQL, CockroachDB",
            "NoSQL, MongoDB",
            "Redis, RabbitMQ",
            "Mocha.js, Gulp.js",
            "Jmeter",
            "Selenium",
            "Cypress",
            "Nightwatch",
            "API Automation",
            "UI Automation",
            "Performance Testing",
            "Jenkins CI/CD",
            "Git, Docker, K8s",
            "Groovy, Shell Scripting",
            "Elastic Search, Kibana",
            "Debugging & RCA",
            "Jira, Rancher, Grafana, Cronicle",
            "Watcher & Pager Duty",
            "Leadership & Mentoring"
        ],
        'experience': [
            {
                'company': 'Samsung Electronics America - Digital E-Commerce, Chennai, India',
                'role': 'SENIOR SOFTWARE DEVELOPMENT ENGINEER IN TEST',
                'period': '2019 - Present',
                'tasks': [
                    'Contributed to core backend team responsible for delivering major features from requirements definition through successful deployment, within exceedingly tight deadlines across various micro services.',
                    'Responsible for creating end-to-end architecture design for implementing Gift-cards, Wallet and Dropshipping in the SEA Platform. Hands on experience on working with 3rd party apis.',
                    'Supervised and lead a team of 3 junior software engineer interns during the development of dropshipping , resulted in 2% of overall revenue increase within 3 months',
                    'Introduced a feature to reduce the cancellation rates by giving discounts after considering various user parameters, resulted in 40% drop in cancellation rate within a year.',
                    'Enhanced the application\'s features to effectively fix the bugs and optimize the overall performance and user experience. Worked on various production data fixes which unblocks the order flow in order to increase the overall customer experience.',
                    'Took responsibility to do RCA for production bugs and provide proper explanations/logging details to the respected team in order to resolve the customer issues.',
                    'During various launches and releases, created visualizations and dashboards in kibana which helps people to quickly identity the issues during the prod monitoring. Developed a Single page Application for visualising the production performance metrics using Vue.js & React.js.',
                    'Owned the Pager duty setup for the micro-services owned and ensured necessary logging/pd\'s created for new changes. Hands on experience on writing watcher scripts.',
                    'Coordinated with QA team on monitoring/troubleshooting production after each sprint release. During launches, on call support with cross functional teams to ensure a seamless launch.',
                    'Hands on experience on writing and maintaining unit tests and mock tests. Have worked on setting up CI/CD pipelines in Jenkins so that each merge request will go through standard set of testing models before it can be merged.'
                ]
            }
        ],
        'interests': [
            'Writing Short stories',
            'Social media influencing',
            'Reading books'
        ],
        'languages': [
            {
                'language': 'English',
                'proficiency': 'Professional Working Proficiency'
            },
            {
                'language': 'Tamil',
                'proficiency': 'Native or Bilingual Proficiency'
            }
        ],
        'awards': [
            {
                'award': 'Inspiring Others',
                'awarded_by': 'Samsung Electronics America - Q2 2020 Awards'
            },
            {
                'award': 'Rising Star - 2020',
                'awarded_by': 'Samsung Electronics - People\'s Choice Award'
            }, 
            {
                'award': 'Maximal Ideas Implemented',
                'awarded_by': 'Samsung Electronics America - Hackathon\'20'
            }, 
            {
                'award': 'Inspiring Others',
                'awarded_by': 'Samsung Electronics America - Q2 2020 Awards'
            }, 
            {
                'award': 'Inspiring Others',
                'awarded_by': 'Samsung Electronics America - Q2 2020 Awards'
            }, 
            {
                'award': 'Inspiring Others',
                'awarded_by': 'Samsung Electronics America - Q2 2020 Awards'
            }
        ]
    }
    return render(request, 'index.html', context)
