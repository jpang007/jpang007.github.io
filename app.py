import analytics
analytics.write_key = '{REPLACE_WITH_YOUR_WRITE_KEY}'

# Scenario 1: a new user comes to site and submits an inquiry with their email address
# Fire a track event to capture the inquiry
# Track event: no userId, event Name, Properties, no context/options updates, anonymousId
analytics.track(None, 'Inquiry Submitted', {
                'contact_preference': 'email', 'inquiry_type': 'Request More Information'}, None, None, 'b2bf6bf2-7cda-42d6-a65a-01582392588f')

# Fire an identify event to capture the email
# Identify event: no userId, traits, no context/options updates, anonymousId
analytics.identify(None, {'email': 'jason@yahoo.com'},
                   None, None, 'b2bf6bf2-7cda-42d6-a65a-01582392588f')

# Scenario 2: a new signs up for an account and is assigned a persistent userId
# Fire an identify event to capture the users' userid
# Identify event: userId, traits, no context/options updates, anonymousId
analytics.identify('1423423534534535', {'name': 'Bruce Lee', 'account_type': 'free',
                   'opt_in': 'false'}, None, None, 'b2bf6bf2-7cda-42d6-a65a-01582392588f')

# Fire a track event to capture the account creation
# Track event: userId, event Name, No properties, no context/options updates, anonymousId
analytics.track('1423423534534535', 'Account Created', None,
                None, None, 'b1bf9bf1-7cda-42c6-a75a-015823925aa5')
