
import wavefront_api_client as wave_api

base_url = 'https://dev.corp.wavefront.com'
api_key = '2cd10ec2-0932-434d-b773-c237ca938537'


client = wave_api.ApiClient(host='https://dev.corp.wavefront.com', header_name='Authorization', header_value='Bearer ' + api_key)

# instantiate source API
metric_api = wave_api.MetricApi(client)

response = metric_api.get_metric_details("cpu.usage.idle")

print response