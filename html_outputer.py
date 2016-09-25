#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<meta charset=\"utf-8\">")
        fout.write("<body>")
        fout.write("<table  rules=rows>")
        fout.write("<tr>")
        fout.write("<td>姓名</td>")
        fout.write("<td>性别</td>")
        fout.write("<td>部门</td>")
        fout.write("<td>研究方向</td>")
        fout.write("<td>邮件地址</td>")
        fout.write("<td></td>")
        fout.write("<td colspan=\"5\">个人简介</td>")
        fout.write("<td></td>")
        #fout.write("<td colspan=\"5\">科研情况</td>")
        #fout.write("<td></td>")
        #fout.write("<td colspan=\"5\">获奖情况</td>")
        #fout.write("<td></td>")
        fout.write("<td colspan=\"5\">备注</td>")
        fout.write("</tr>")
        try:
            for data in self.datas:
            
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['CName'])
                fout.write("<td>%s</td>" % data['Sex'])
                fout.write("<td>%s</td>" % data['GroupID'])
                fout.write("<td>%s</td>" % data['U_searchD'])
                fout.write("<td>%s</td>" % data['Email'])
                fout.write("<td>%s</td>" % data['Profile'])
                #fout.write("<td>%s</td>" % data['Program'].encode('utf-8'))
                #fout.write("<td>%s</td>" % data['Reward'])
                fout.write("<td>%s</td>" % data['Tip'])
                fout.write("</tr>")
        except:
            pass
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()