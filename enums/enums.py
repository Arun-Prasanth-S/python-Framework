from enum import Enum

class HeaderMenuItemsEnum(Enum):
    WhyTendableWithSpecialCharacter = "Why Tendable?"
    WhyTendable = "Why Tendable"
    OurStory = "Our Story"
    OurSolution = "Our Solution"
    RequestADemo = "Request A Demo"
    ContactUs = "Contact Us"

class FormEnum(Enum):
    FullName = "fullName"
    OrganisationName = "organisationName"
    CellPhone = "cellPhone"
    Email = "email"
    JobRole = "jobRole"

class ContactDetailsEnum(Enum):
    FullName = "Arun"
    OrganisationName = "SoftSuave"
    CellPhone = "123456789"
    Email = "Arun@gmail.com"

class JobRoleEnum(Enum):
    JobRole = "Job Role"
    ExecutiveBoardMember = "Executive Board Member"
    Management = "Management"
    CNO = "CNO"
    FrontlineWorker = "Frontline worker"
