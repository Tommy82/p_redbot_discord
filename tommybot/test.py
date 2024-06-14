import aiohttp
import asyncio
import json

personalToken = '' #Personal Token
headers = {'Authorization': 'Bearer ' + personalToken}

async def call_api(url, headers, params):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url, params=params) as response:
            resp = await response.read()
            return resp

async def getCompanies(headers):
    url = 'https://api.statev.de/req/factory/list'
    resp = await call_api(url, headers, {})
    companiesObj = json.loads(resp)
    return companiesObj

async def getCompanyInventory(headers, companyID):
    url = 'https://api.statev.de/req/factory/inventory/' + companyID
    resp = await call_api(url, headers, {})
    inventoryObj = json.loads(resp)
    return inventoryObj


companies = asyncio.run(getCompanies(headers))
if ( companies and len(companies) > 0 ):
    for company in companies:
        companyID = company['id']
        inventory = asyncio.run(getCompanyInventory(headers, companyID))
        print(inventory)

#asyncio.run(push())