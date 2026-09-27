def combine_files(file_paths: list, output_filename: str) -> None:
    files_data = []

    for path in file_paths:
        with open(path) as infile:
            lines = infile.readlines()
            files_data.append({"filename": path, "count": len(lines), "content": lines})

    files_data.sort(key=lambda x: x["count"])

    with open(output_filename, "w") as outfile:
        for d in files_data:
            outfile.write(f"{d["filename"]}\n")
            outfile.write(f"{d["count"]}\n")

            outfile.writelines(d["content"])

            if d["content"] and not d["content"][-1].endswith("\n"):
                outfile.write("\n")


combine_files(["1.txt", "2.txt", "3.txt"], "4.txt")
