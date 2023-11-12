import os
import tabula
try:
    mainpath = r'C:\dev\asanas'  # Use raw string for Windows paths
    path = os.path.join(mainpath, "PDF") + os.sep
    savepath = os.path.join(mainpath, "output") + os.sep

    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(savepath):
        os.mkdir(savepath)

    a = []
    val = 0
    ent = os.listdir(path)
    for en in ent:
        if en.lower().endswith('.pdf'):  # Ensure it's a PDF
            a.append(en)

    for i in range(len(a)):
        print("Converting", a[val], ".......")
        fname = path + a[val]
        out = savepath + a[val] + ".csv"
        tabula.convert_into(fname, out, output_format="csv", pages='all')
        print("\nFile '" + a[val] + ".csv' saved.")
        val += 1

except Exception as e:
    print("Something went wrong! Please try again!")
    print(str(e))  # To see the actual error message
