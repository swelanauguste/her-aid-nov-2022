import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Donation

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(STATUS=400)
    
    if event.type == 'checkout.session.completed':
        session = event.data.object
        session_id = event['data']['object']['id']
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                donation = Donation.objects.get(check_out_id=session_id)
            except Donation.DoesNotExist:
                return HttpResponse(status=400)
            donation.donated = True
            donation.stripe_id = session.payment_intent
            donation.save()
    return HttpResponse(status=200)