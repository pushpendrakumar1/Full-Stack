import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "table.settings")
django.setup()

from myapp.models import activitylists, clientname, operator  # Import your model

from random import choice

# Get all client and operator IDs
client_ids = clientname.objects.values_list('id', flat=True)
operator_ids = operator.objects.values_list('id', flat=True)

instances = []
num_entries = 3000

for i in range(num_entries):
    client_id = choice(client_ids)
    operator_id = choice(operator_ids)

    client_instance = clientname.objects.get(pk=client_id)
    operator_instance = operator.objects.get(pk=operator_id)

    data_record = {
        'client': client_instance,
        'operator': operator_instance,
        'oem': 'Nokia',
        'Ticket_Number': 12345,
        'fa_location': 'Location 1',
        'site_ids': 'Site 1, Site 2',
        'Added_Date': '2023-06-01',
        'County': 'County 1',
        'Activity': 'IX',
        'Ix_Date': '2023-06-10',
        'G_IX_date': '23',
        'Ticket_Status': 'Open',
        'lite_site_id': 'Lite Site 1',
        'three_g_site_id': '3G Site 1',
        'Field_Installation': 'F',
        'Alarm': 'A',
        'Field_Integration': 'FI',
        'remote_Integration': 'R',
        'five_g_site_id': '5G Site 1',
        'site_name': 'Site Name 1',
        'market': 'Market 1',
        'address': 'Address 1',
        'zip_code': '12345',
        'Added_By': 'John Doe',
        'IX_Status': 'Completed',
        'CX_Status': 'Pending',
        'latitude': '123.456',
        'longitude': '78.901',
        'mon_hours': '00:00::00:59',
        'tue_hours': '00:00::00:59',
        'wed_hours': '00:00::00:59',
        'thu_hours': '00:00::00:59',
        'fri_hours': '00:00::00:59',
        'sat_hours': '00:00::00:59',
        'sun_hours': '00:00::00:59',
        'key_comments': 'Some comments',
        'notice_needed': 'Yes',
        'notice_comments': 'Notice comments',
        'num_of_carrier': 2,
        'pace': 'Normal',
        'ptn': 'PTN 1',
        'sow_type': 'Option 1',
        'wo_cr_id': 'WO/CR 1',
        'sow': 'SOW 1',
        'ix_schedule_date': '2023-06-20',
        'nest': 'Yes',
        'mop_start_time': '10:00',
        'mop_end_time': '12:00',
        'ix_date_comment': 'Some comment',
        'equipment_pickup': 'Option 1',
        'five_g_ix_standalone': 'Option 2',
        'five_g_ix_schedule_date': '2023-06-25',
        'call_test_date': '2023-06-28',
        'market_state': 'State 1',
        'crew_dispatch_date': '2023-06-05',
    }
    # ...


    instance = activitylists(**data_record)
    instances.append(instance)

activitylists.objects.bulk_create(instances)