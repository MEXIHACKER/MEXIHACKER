import requests, re , colorama
colorama.init()
print("""
\033[1;31m\033[1;37m ██████╗ █████╗ ███╗   ███╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██╔════╝██╔══██╗████╗ ████║      ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
██║     ███████║██╔████╔██║█████╗███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗
██║     ██╔══██║██║╚██╔╝██║╚════╝██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
╚██████╗██║  ██║██║ ╚═╝ ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║
\033[1;31m ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
\033[1;31m                                                                        EDICION MEJORADA 
\033[1;31m1) \033[1;37mEstados Unidos               \033[1;31m31) \033[1;37mMexico                \033[1;31m61) \033[1;37mMoldova
\033[1;31m2) \033[1;37mJapon                        \033[1;31m32) \033[1;37mFinlandia             \033[1;31m62) \033[1;37mNicaragua
\033[1;31m3) \033[1;37mItalia                       \033[1;31m33) \033[1;37mChina                 \033[1;31m63) \033[1;37mMalta
\033[1;31m4) \033[1;37mcorea                        \033[1;31m34) \033[1;37mChile                 \033[1;31m64) \033[1;37mTrinidad y Tobago
\033[1;31m5) \033[1;37mFrancia                      \033[1;31m35) \033[1;37mSudafrica             \033[1;31m65) \033[1;37mArabia Saudita
\033[1;31m6) \033[1;37mAlemania                     \033[1;31m36) \033[1;37mEslovaquia            \033[1;31m66) \033[1;37mCroacia
\033[1;31m7) \033[1;37mTaiwan                       \033[1;31m37) \033[1;37mHungria               \033[1;31m67) \033[1;37mChipre
\033[1;31m8) \033[1;37mFederacion Rusa              \033[1;31m38) \033[1;37mIrlanda               \033[1;31m68) \033[1;37mPakistan
\033[1;31m9) \033[1;37mReino Unido                  \033[1;31m39) \033[1;37mEgipto                \033[1;31m69) \033[1;37mEmiratos Arabes Unidos
\033[1;31m10) \033[1;37mPaises Bajos                \033[1;31m40) \033[1;37mTailandia             \033[1;31m70) \033[1;37mKazajistan
\033[1;31m11) \033[1;37mRepublica Checa             \033[1;31m41) \033[1;37mUcrania               \033[1;31m71) \033[1;37mKuwait
\033[1;31m12) \033[1;37mTurquia                     \033[1;31m42) \033[1;37mSerbia                \033[1;31m72) \033[1;37mVenezuela
\033[1;31m13) \033[1;37mAustria                     \033[1;31m43) \033[1;37mHong Kong             \033[1;31m73) \033[1;37mGeorgia
\033[1;31m14) \033[1;37mSuiza                       \033[1;31m44) \033[1;37mGrecia                \033[1;31m74) \033[1;37mMontenegro
\033[1;31m15) \033[1;37mEspaña                      \033[1;31m45) \033[1;37mPortugal              \033[1;31m75) \033[1;37mEl Salvador
\033[1;31m16) \033[1;37mCanada                      \033[1;31m46) \033[1;37mLetonia               \033[1;31m76) \033[1;37mLuxemburgo
\033[1;31m17) \033[1;37mSuecia                      \033[1;31m47) \033[1;37mSingapur              \033[1;31m77) \033[1;37mCuracao
\033[1;31m18) \033[1;37mIsrael                      \033[1;31m48) \033[1;37mIslandia              \033[1;31m78) \033[1;37mPuerto Rico
\033[1;31m19) \033[1;37mIran                        \033[1;31m49) \033[1;37mMalasia               \033[1;31m79) \033[1;37mCosta Rica
\033[1;31m20) \033[1;37mPolonia                     \033[1;31m50) \033[1;37mColombia              \033[1;31m80) \033[1;37mBielorrusia
\033[1;31m21) \033[1;37mIndia                       \033[1;31m51) \033[1;37mTunez                 \033[1;31m81) \033[1;37mAlbania
\033[1;31m22) \033[1;37mNoruega                     \033[1;31m52) \033[1;37mEstonia               \033[1;31m82) \033[1;37mLiechtenstein
\033[1;31m23) \033[1;37mRumania                     \033[1;31m53) \033[1;37mRepublica Dominicana  \033[1;31m83) \033[1;37mBosnia y Herzegovia
\033[1;31m24) \033[1;37mVietnam                     \033[1;31m54) \033[1;37mEslovenia             \033[1;31m84) \033[1;37mParaguay
\033[1;31m25) \033[1;37mBelgica                     \033[1;31m55) \033[1;37mEcuador               \033[1;31m85) \033[1;37mFilipinas
\033[1;31m26) \033[1;37mBrasil                      \033[1;31m56) \033[1;37mLituania              \033[1;31m86) \033[1;37mIslas Faroe
\033[1;31m27) \033[1;37mBulgaria                    \033[1;31m57) \033[1;37mPalestina             \033[1;31m87) \033[1;37mGuatemala
\033[1;31m28) \033[1;37mIndonesia                   \033[1;31m58) \033[1;37mNueva Zelanda         \033[1;31m88) \033[1;37mNepal
\033[1;31m29) \033[1;37mDinamarca                   \033[1;31m59) \033[1;37mBangladesh            \033[1;31m89) \033[1;37mPeru
\033[1;31m30) \033[1;37mArgentina                   \033[1;31m60) \033[1;37mPanama                \033[1;31m90) \033[1;37mUruguay
                                                          \033[1;31m91) \033[1;37mExtra
""")

try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("ELIGE UNA OPCION : "))
    if num not in range(1, 91+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"https://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()