#Level 17 → 18

### 📝 Level Objective
The password for the next level is stored in a file called **passwords.new** and is the only line that has been changed between **passwords.old** and **passwords.new**.

### 🛠️ Walkthrough
Instead of manually inspecting hundreds of lines, I used the `diff` utility to compare the two files and isolate the unique entry.

1.  **Identify the files:** Located in the home directory were `passwords.old` and `passwords.new`.
2.  **Run the comparison:**
    ```bash
    bandit17@bandit:~$ diff passwords.new passwords.old
    ```
3.  **Analyze the output:** The command returned a specific line indicating the divergence between the two files. The password was found in the version belonging to the "new" file.

---

### 🔍 Understanding the `diff` Output
When you run `diff`, the output tells you exactly how to change the first file to match the second file. Here is the breakdown of the result seen in the terminal:

**Output:**
```text
42c42
< x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
---
> KxOU4IzbXM8j8HeAWPAXTd1eC77mp1qV
```

* **`42c42`**: This means line **42** of the first file needs to be **changed (c)** to match line **42** of the second file.
* **`<` (Less than symbol)**: Indicates content present in the **first file** (`passwords.new`).
* **`---`**: A separator between the two files' content.
* **`>` (Greater than symbol)**: Indicates content present in the **second file** (`passwords.old`).

> 
Since we needed the password from the "new" file, the line marked with `<` was our target.

---

### 💡 What I Learned

* **Efficient Comparison**: `diff` is the industry standard for comparing configuration files, source code, or logs to find specific changes without manual scrolling.
* **Normal Output Format**: By default, `diff` uses a concise format (`42c42`) to describe changes. The letters you'll see most often are:
    * **`a`**: Addition
    * **`d`**: Deletion
    * **`c`**: Change
* **Reading the Man Pages**: Using `man diff` helped clarify that the order of the files in the command determines which symbols (`<` or `>`) represent which file.

---

**Next Level Password:** `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`
