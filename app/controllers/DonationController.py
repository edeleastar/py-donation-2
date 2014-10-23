from flask import render_template, url_for, redirect, request
from app.models.Donaton import Donation

from . import donate

@donate.route('/donation')
def index():
  return render_template('donationcontroller/index.html')

@donate.route('/donation/donate', methods=['POST'])
def donateAmount():
  donation = Donation(request.form['amountDonated'], request.form['methodDonated'], ID=Donation.objects.count() + 1)
  donation.save()
  return redirect('/donation')

@donate.route('/donation/report')
def report():
  return render_template('donationcontroller/report.html', donations=Donation.objects())