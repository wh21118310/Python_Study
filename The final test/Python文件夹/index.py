#DataBase author:李东徽
#Tkinter author:周明蕾 苏轩
#The last texter:李东徽
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox
import tkinter.filedialog
import sqlite3
import xlrd
class Information:
    def __init__(self,master=None):
        self.root = master;
        self.root.geometry('400x250')
        self.root.title('导入信息')
        self.con = sqlite3.connect('match.db')
        self.page = Frame(self.root)
        self.creatapage()
    def creatapage(self):
        Label(self.page).grid(row = 0)
        Button(self.page,text="导入文件",command = self.choose).grid(row = 2,stick = W,pady = 10)
        Button(self.page,text="取消导入",command= self.exitimport).grid(row = 2,stick = E,column = 1)
        self.page.pack()
    def exitimport(self):
        if tkinter.messagebox.askyesno("取消", "确认取消导入吗"):
            self.page.destroy()
            self.con.close()
    def choose(self):
        filename = tkinter.filedialog.askopenfilename()
        if filename != '':
            book = xlrd.open_workbook(filename)
            for sheet in book.sheets():
                if sheet.nrows > 0 and sheet.ncols > 0:
                    for row in range(1, sheet.nrows):
                        row_data = []
                        for col in range(sheet.ncols):
                            data = sheet.cell(row, col).value
                            # excel表格内容数据类型转换 float -> int
                            if type(data) is float: data = int(data)
                            row_data.append(data)
                        if len(row_data) > 0:
                            print(row_data)
                            # 打开数据库(不存在是会创建数据库)
                            self.con = sqlite3.connect('match.db')
                            cur = self.con.cursor()
                            try:
                                cur.execute(
                                    'create table if not exists user(id varchar(13)primary key, class varchar(15),name  varchar(15), tel varchar (13) ,WeChat varchar(13))')
                                cur.execute("insert into user(id,class,name,tel,WeChat) values(?,?,?,?,?)", row_data)
                                self.con.commit()
                            except sqlite3.Error as e:
                                print("An error occured:%s", e.args[0])
                            finally:
                                cur.close()
                                self.con.close()
        else:
            tkinter.messagebox.showerror('错误','您未导入excel文件')
class Change:
    def __init__(self,master=None):
        self.root = master
        self.root.title('信息更改')
        self.root.geometry("400x250")
        self.conn = sqlite3.connect('match.db')
        self.id = StringVar()
        self.select = StringVar()
        self.mody = StringVar()
        self.page = Frame(self.root)
        self.creatapage()
    def creatapage(self):
        Label(self.page).grid(row = 0)
        Label(self.page,text='请输入更改项并输入学号').grid(row = 1,pady = 10,sticky = W)
        Entry(self.page,textvariable = self.select,width = 12).grid(row = 1,column = 1)
        Entry(self.page,textvariable=self.id,width=12).grid(row = 1,column = 6)
        Label(self.page,text='请输入更改内容' ).grid(row = 3,pady = 10,sticky = W)
        Entry(self.page,textvariable = self.mody,width = 12).grid(row = 3,column = 1,sticky = E)
        Button(self.page, text='确认',command = self.SubmitChange).grid(row=5, pady = 10,sticky = W)
        Button(self.page, text='取消', command=self.exitchange).grid(row=5, column = 1,sticky = E)
        self.page.pack()
    def exitchange(self):
        if tkinter.messagebox.askyesno("取消", "确认取消更改吗"):
            self.page.destroy()
            self.conn.close()
    def  SubmitChange(self):
        cur = self.conn.cursor()
        sql = 'select * from user where id = "%s"'%self.id.get()
        cur.execute(sql)
        i = 0
        for x in cur.fetchall():
            i += 1
        if i == 0 :
            tkinter.messagebox.showerror('错误','查无此人')
        else:
            if self.select.get() == 'id':
             cur.execute( 'update user set id = ? where  id = ? ',(self.mody.get(),self.id.get()))
             self.conn.commit()
             tkinter.messagebox.showinfo('更改成功','信息已更改')
            elif self.select.get() == 'class':
                cur.execute('update user set class = ? where  id = ? ', (self.mody.get(), self.id.get()))
                self.conn.commit()
                tkinter.messagebox.showinfo('更改成功', '信息已更改')
            elif self.select.get() == 'name':
                cur.execute('update user set name = ? where  id = ? ', (self.mody.get(), self.id.get()))
                self.conn.commit()
                tkinter.messagebox.showinfo('更改成功', '信息已更改')
            elif self.select.get() == 'tel':
                cur.execute('update user set tel = ? where  id = ? ', (self.mody.get(), self.id.get()))
                self.conn.commit()
                tkinter.messagebox.showinfo('更改成功', '信息已更改')
            elif self.select.get() == 'WeChat':
                cur.execute('update user set WeChat = ? where  id = ? ', (self.mody.get(), self.id.get()))
                self.conn.commit()
                tkinter.messagebox.showinfo('更改成功', '信息已更改')

class Seek:
    def __init__(self,master=None):
        self.root = master
        self.root.title('信息查询')
        self.root.geometry("400x250")
        self.con = sqlite3.connect('match.db')
        self.id = StringVar()
        self.page = Frame(self.root)
        self.creatapage()
    def creatapage(self):
        Label(self.page).grid(row = 0)
        Label(self.page,text="请输入需要查询的参赛者学号").grid(row = 1,pady = 10,sticky = W)
        Entry(self.page,textvariable = self.id,width = 12).grid(row = 1,column = 1,sticky = E)
        Button(self.page, text='确认', command=self.SubmitSeek).grid(row=4, pady=10, sticky=W)
        Button(self.page, text='取消', command=self.exitseek).grid(row=4, column=1, sticky=E)
        self.page.pack()
    def exitseek(self):
        if tkinter.messagebox.askyesno("取消", "确认要取消查询吗"):
            self.page.destroy()
            self.con.close()
    def SubmitSeek(self):
        cur = self.con.cursor()
        sql = 'select * from user where id = "%s"'%self.id.get()
        cur.execute(sql)
        i = 0
        for (a,b,c,d,e) in cur.fetchall():
            i += 1
            tkinter.messagebox.showinfo('查找结果', '学号：%s\n班级：%s\n姓名：%s\n电话：%s\n微信号：%s\n' % (a, b, c, d,e))
        if i == 0:
            tkinter.messagebox.showerror('查找错误','查无此人，请重新输入!')
class Index:
    def __init__(self,master):
        self.root = master
        self.root.title("系统后台")
        self.root.geometry("400x250")
        self.root.protocol("WM_DELETE_WINDOW",exit)
        self.page = Frame(self.root)
        self.creatapage()
    def creatapage(self):
        Label(self.page).grid(row = 0)
        Button(text='导入信息', command=self.InformationPage).place(x=0,y=0)
        Button(text='信息查询', command=self.SeekPage).place(x=0,y=40)
        Button(text='信息更改', command=self.ChangePage).place(x=0,y=80)
        Button(root, text='  退出  ', command=self.root.quit).place(x=0,y=120)
        self.page.pack()
    def InformationPage(self):
        self.page.destroy()
        Information(self.root)
    def SeekPage(self):
        self.page.destroy()
        Seek(self.root)
    def ChangePage(self):
        self.page.destroy()
        Change(self.root)
    def exit(self):
        if tkinter.messagebox.askyesno("退出", "确认退出吗"):
            self.page.destroy()
if __name__ == '__main__':
    root = Tk()
    Index(root)
    root.mainloop()

