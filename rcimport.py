#!/usr/bin/python
# -*- coding: utf-8 -*-

import kickerrankade

kickername_rankadename_mapping = {
    u"康凯":u"尹康凯",
    u"尹康凯":u"尹康凯",
    u"孟晓然":u"*Meng Xiaoran",
    u"晓然":u"*Meng Xiaoran",
    u"赵瑞华":u"Zhaoruihua",
    u"曹聃":u"曹先森",
    u"曹凯":u"*Cao Kai",
    u"慧芳":u"*Liu Huifang",
    u"刘慧芳":u"*Liu Huifang",
    u"施磊":u"*Shi Lei",
    u"任恬":u"*Ren Tian",
    u"Ren Tian":u"*Ren Tian",
    u"苏本昌":u"苏本昌",
    u"本昌":u"苏本昌",
    u"肖晓林":u"*Xiao Xiaolin",
    u"晓林":u"*Xiao Xiaolin",
    u"国祝":u"*guozhu",
    u"张小武":u"XiaowuZhang",
    u"张晓武":u"XiaowuZhang",
    u"韩广义":u"HanGuangyi",
    u"广义":u"HanGuangyi",
    u"Matt":u"*matt",
    u"张茜明":u"zhangximing",
    u"茜明":u"zhangximing",
    u"博士":u"*boshi",
    u"鑫岩":u"Xinyan Xing",
    u"邢鑫岩":u"Xinyan Xing",
    u"Lisa":u"*Lisa",
    u"lisa":u"*Lisa",
    u"关剑喜（替补）":u"*guanjianxi",
    u"关剑喜":u"*guanjianxi",
    u"彭亚":u"*Peng Ya",
    u"Peng Ya":u"*Peng Ya",
    u"教练":u"*Gu Yafei",
    u"Yu Yunda":u"*Yu Yunda",
    u"于运达":u"*Yu Yunda",
    u"运达":u"*Yu Yunda",
    u"高飞":u"*Gao Fei",
    u"lily":u"Lilyhao",
    u"郝思涵":u"Lilyhao",
    u"秦岭":u"Ling Qin",
    u"qinling":u"Ling Qin",
    u"陶见涛":u"*Tao Jiantao",
    u"陶建涛":u"*Tao Jiantao",
    u"建涛":u"*Tao Jiantao",
    u"米思远":u"*Mi Siyuan",
    u"小芈":u"*Mi Siyuan",
    u"小米":u"*Mi Siyuan",
    u"雷霞":u"*Lei Xia",
    u"金龙":u"蔡金龙",
    u"蔡金龙":u"蔡金龙",
    u"赵全国":u"*Zhao Quanguo",
    u"全国":u"*Zhao Quanguo",
    u"李绍铭":u"*Li Shaoming",
    u"陈珍":u"*Chen Zhen",
    u"曹兰笛":u"*caolandi",
    u"杨芃林":u"*Yang Penglin",
    u"欧阳洋":u"*Ou Yangyang",
    u"佐罗":u"*Zuo Luo",
    u"Allen":u"allenlian",
    u"Amber":u"amberlin",
    u"Embbnux":u"embbnux",
    u"Ethan":u"*ethan.chen",
    u"Holly":u"*holly.wu",
    u"Ian":u"*ian.zhang",
    u"JacobJiang":u"JacobJiang",
    u"Jerry":u"*jerry.cai",
    u"John":u"*john.lin",
    u"Josie":u"*josie.zhang",
    u"Lewi":u"*lewi.li",
    u"Lip":u"LipWang",
    u"Nasen":u"NasenYou",
    u"Ned":u"*ned.le",
    u"Samuel":u"SamuelHuang",
    u"Steve":u"*steve.chen",
    u"Tony":u"*tony.lin",
    u"Yeoman":u"*yeoman.cai",
    u"Joey":u"会拉射的大菜鸡",
    u"Vincent":u"铃盛纹身特"
}

playground = "RingCentral Xiamen Fitness Room"
groupname = "RC Foosball"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print "Usage: %s xxx.ktool username passwd <skip>" % sys.argv[0]
        print "\t xxx.ktool: file exported from kickertool"
        print "\t username/passwd: your rankade user/pass"
        sys.exit(0)

    start = sys.argv[4] if len(sys.argv) > 4 else 1
    kickerrankade.main(sys.argv[1], sys.argv[2], sys.argv[3],
                       playground,
                       groupname,
                       kickername_rankadename_mapping,
                       start)
