'''
Created on Feb 10, 2018

@author: smckinney
'''
from email._header_value_parser import DisplayName


class User:    
    "Fortess User"

    def __init__(
            self,
            uid=None,
            password=None,
            ou=None,
            internalId=None,
            roles=None,
            pwPolicy=None,
            cn=None,
            sn=None,
            dn=None,
            description=None,
            displayName=None,
            employeeType=None,
            title=None,
            phones=None,
            mobiles=None,
            emails=None,
            
            
            
            #constraint=None,
            
            
            
#             x=None,
#             x=None,
#             x=None,
#             x=None,
#             x=None,
#             x=None,
                        
            ):
        self.uid = uid
        self.password = password
        self.ou = ou
        self.internalId = internalId
        self.roles = roles
        self.pwPolicy = pwPolicy        
        self.cn = cn       
        self.sn = sn
        self.dn = dn
        self.description = description
        self.displayName = displayName
        self.employeeType = employeeType
        self.title = title
        self.phones = phones
        self.mobiles = mobiles
        self.emails = emails
        
        
        #self.constraint = constraint
        
#         self.x = x
#         self.x = x
#         self.x = x
#         self.x = x
#         self.x = x
#         self.x = x
#     private boolean reset;
#     private boolean locked;
#     private Boolean system;
#     private Props props = new Props();
#     private Address address;
#     private List<String> phones;
#     private List<String> mobiles;
#     private List<String> emails;

#     private List<UserRole> roles;
#     private List<UserAdminRole> adminRoles;
#     @XmlTransient
#     private byte[] jpegPhoto;
# 
#     // RFC2307bis:
#     /*
#     MUST ( cn $ uid $ uidNumber $ gidNumber $ homeDirectory )
#     MAY ( userPassword $ loginShell $ gecos $ description ) )
#      */
#     private String uidNumber;
#     private String gidNumber;
#     private String homeDirectory;
#     private String loginShell;
#     private String gecos;
        
#             beginTime=None,
#             endTime=None,
#             beginDate=None,
#             endDate=None,
#             beginLockDate=None,
#             endLockDate=None,
#             dayMask=None,
#     private int timeout;

#         self.beginTime = beginTime
#         self.endTime = endTime
#         self.beginDate = beginDate
#         self.endDate = endDate
#         self.beginLockDate = beginLockDate
#         self.endLockDate = endLockDate
#         self.dayMask = dayMask
