import datetime
import json
import logging
import os
import sys
import re
import requests
#import zeep
from requests import Session
import xml.etree.ElementTree as ET
import xmltodict
#import warnings
#warnings.filterwarnings("ignore")



def Handle_XMl_File(response):
    # Extract the content from the response
    content = response.content
    LOGGER.info("XML Response Content: %s", content)
    tree = ET.ElementTree(ET.fromstring(content))
    root = tree.getroot()
    tree = ET.ElementTree(root)
    ET.indent(tree, '  ')
    xmlstr = ET.tostring(root, encoding='utf8', method='xml')
    xmlstr=xmlstr.decode('utf-8')
    xml_dict=xmltodict.parse(xmlstr)
    
    
    

    #Extract Name Data
    first_name_eng=xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:PersonalInfo"]["ns1:FirstName"]
    middle_name_eng=xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:PersonalInfo"]["ns1:MiddleName"]
    last_name_eng=xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:PersonalInfo"]["ns1:LastName"]
    first_name_arabic=xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:PersonalInfo"]["ns1:FirstNameAr"]
    middle_name_arabic=xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:PersonalInfo"]["ns1:MiddleNameAr"]
    last_name_arabic=xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:PersonalInfo"]["ns1:LastNameAr"]
    

    #Phone Number Data
    phone_country_code = xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:ContactInfo"]["ns1:PhoneDtls"]["ns1:PhoneCountryCode"]
    phone_area_code = xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:ContactInfo"]["ns1:PhoneDtls"]["ns1:PhoneAreaCode"]
    phone_number=xml_dict["ns0:Envelope"]["ns0:Body"]["ns1:CustDtlsInqRs"]["ns1:Body"]["ns1:ContactInfo"]["ns1:PhoneDtls"]["ns1:PhoneNum"]
        
    

    

    return {
        "udf_sline_302": f"{first_name_eng} {middle_name_eng} {last_name_eng}",
        "udf_sline_301": f"{first_name_arabic} {middle_name_arabic} {last_name_arabic}",
        "udf_sline_303": f"{phone_country_code} {phone_area_code} {phone_number}"
    }



