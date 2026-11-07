# import qrcode 
# ##strip func se extra whitespaces ka masla khatam hojayega 
# url=input("enter the url for qr code:").strip()

# file_path= "C:\\python folders\\qrcode.png"
# #yaha pr agar kuch specific path send kroge to png waha save hojaygi 
# #wrna jaha ye folder and iske files khule h auto. waha save hojaeygi
 
# qr=qrcode.QRCode()
# qr.add_data(url)

# img = qr.make_image()
# img.save(file_path)
# print("successfully your qr code has been generated!")

#in code se basic wala qrcode generate hoga black-white with fixed size etc.



#BUT KHUD KE DIMESNION,COLOR WALA CHAHIYE TO YE CODE USE KRO 
# import qrcode
# def generate_qr_code(url,file_name):
#     qr=qrcode.QRCode(
#        version=1,
#        error_correction=qrcode.constants.ERROR_CORRECT_L,
#        box_size=10,
#        border=4
#     )
#     qr.add_data(url)
#     qr.make(fit=True)

#     img=qr.make_image(fill_color="white",back_color="purple")
#     img.save(file_name)

#     print("your qr code has been successfully generated!")

# generate_qr_code("https://github.com/hashmi-farhan/contact-book/tree/master","github_qr.png")