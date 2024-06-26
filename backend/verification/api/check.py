from api import models


def check_id_card(credentials: dict) -> tuple[bool, str]:
    verdict = models.FakeIDCardDB.objects.filter(
        issue_date=credentials['issue_date'],
        doc_number=credentials['doc_number'],
        ssn=credentials['ssn']).values("verdict")

    print(credentials)
    print(verdict)
    print(verdict[0]['verdict'])

    if not verdict:
        print("wr here")
        return False, "invalid_credentials"

    if verdict == "valid":
        print("true")
        return True, "valid"
    else :
        return False, verdict[0]['verdict']


def check_driver_license(credentials: dict) -> tuple[bool, str]:
    verdict = models.FakeDriverLicenseDB.objects.filter(
        license_number=credentials['license_number'],
        valid_date=credentials['valid_date']).values("verdict")
    
    print(credentials)
    print(verdict)
    print(verdict[0]['verdict'])

    if not verdict:
        return False, "invalid_credentials"

    if verdict == "valid":
        return True, "valid"
    else :
        return False, verdict[0]['verdict']

# TODO implement passport check
def check_passport(credentials: dict) -> tuple[bool, str]:
    pass


def check_sat(credentials: dict) -> tuple[bool, str]:
    verdict = models.FakeSATDB.objects.filter(
        unique_number=credentials['unique_number'],
        sat_ssn=credentials['sat_ssn'],
        sat_ict=credentials['sat_ict']).values("verdict")
    
    print(credentials)
    print(verdict)
    print(verdict[0]['verdict'])

    if not verdict:
        return False, "invalid_credentials"

    if verdict == "valid":
        return True, "valid"
    else :
        return False, verdict[0]['verdict']


check = {
    'drivers_license': check_driver_license,
    'passport': check_passport,
    'id': check_id_card,
    'sat': check_sat,
    }