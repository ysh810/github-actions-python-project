from datetime import datetime

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("GitHub Actions Report\n")
    f.write(f"Generated at: {datetime.now()}\n")

print("report.txt 생성 완료")