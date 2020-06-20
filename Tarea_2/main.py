from pack.functions import *

email_1 = 'felix132@gmail.com'
email_2 = 'felix132@gmail.com.mx'
email_3 = 'felix132@gmail5.padts5.com'
fail_email_1 = 'felix132gmail.padts.com'
fail_email_2 = 'felix132@gmail..padts.com'
fail_email_3 = 'as.felix132@gmail.padts.com'
#print(check_email(email_1))


num_1 = '3312345678'
num_2 = '(33)12345678'
num_3 = '(331)1235678'
num_4 = '(33) 1234 5678'
num_5 = '(331)-123-5678'
fail_num_1 = '33312345678'
fail_num_2 = '33 1234-5678'
fail_num_3 = '33fd345678'
#print(check_phone(fail_num_3))


curp_1 = 'GOMF950719HJCDRL00'
curp_2 = 'GOMF950719MJCDRL00'
fail_curp_1 = 'GOMF950719HmJCDRL00'
fail_curp_2 = 'GOMF950719HJCDRLl0'
#print(check_curp(curp_2))


rfc_1 = 'GOMF950719C55'
rfc_2 = 'GOMF9507191H5'
fail_rfc_1 = 'GOM99507191H5'
fail_rfc_2 = 'GOMF95g7191H5'
#print(check_rfc(rfc_1))
