from py2neo import Graph

g = Graph('bolt://localhost:7687')

def get_sv_by_id(id):
   return g.run('MATCH (s:SinhVien) WHERE s.maSV = $ht RETURN s.hoTen', ht = id).evaluate()

def get_list_nganh_by_khoa(tenKhoa):
   return g.run('MATCH (n:Nganh)-[:THUOC]->(k:Khoa) WHERE k.tenKhoa = $tk RETURN n.tenNganh', tk = tenKhoa).data()

def count_number_sv_each_province():
   return g.run('MATCH (s:SinhVien)-[:QUEQUAN]->(t:Tinh) WITH t, COUNT(s) AS SL RETURN t.tenTinh, SL').data()

def find_sv_same_truongPH(maSV):
   return g.run('MATCH (s:SinhVien {maSV: $ma})-[:HOCPT]->(tr:TruongPT) MATCH (s2:SinhVien)-[:HOCPT]->(tr) RETURN s2.hoTen, tr.tenTruong', ma = maSV).data()

def count_sv_each_major_in_each_province():
   return g.run('MATCH (n:Nganh)-[:HOCDH]-(s:SinhVien)-[:QUEQUAN]-(t:Tinh) WITH t, n, COUNT(s) AS SL RETURN t.tenTinh, COLLECT({nganh: n.tenNganh, SL: SL}) AS DS')

def main():
   # print('Câu a')
   # id = input('Nhập mã sinh viên: ')
   # print(get_sv_by_id(id))

   # print('\nCâu b')
   # tenKhoa = input('Nhập tên khoa: ')
   # khoa = get_list_nganh_by_khoa(tenKhoa)
   # for k in khoa:
   #    print(k)

   # print('\nCâu c')
   # tinh = count_number_sv_each_province()
   # for t in tinh:
   #    print(t)

   # print('\nCâu d')
   # maSV = input('Nhập mã sinh viên: ')
   # svCungTruong = find_sv_same_truongPH(maSV)
   # for sv in svCungTruong:
   #    print(sv)

   print('\nCâu e')
   result_e = count_sv_each_major_in_each_province()
   for r in result_e:
      print(r)

if __name__ == "__main__":
   main()