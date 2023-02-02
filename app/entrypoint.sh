#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

# python manage.py flush --no-input

python manage.py migrate
# python manage.py createsuperuser --username king --email no-reply@mail.com --no-input

# python manage.py add_districts
# python manage.py add_locations
# python manage.py add_referral_categories
# python manage.py add_referrals

# python manage.py add_faqs
# python manage.py add_myths_and_facts

# python manage.py add_screening_questions
# python manage.py add_types_of_abuse

# python manage.py add_rights

# python manage.py collectstatic --no-input


exec "$@"