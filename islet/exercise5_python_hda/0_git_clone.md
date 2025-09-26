# Exercise: Cloning a Git Repository

## Objective
Learn how to clone a Git repository into a specific directory on a Linux VM.

---

## Instructions

1. Open a terminal in your VM.

2. Navigate to the target directory where you want to clone the repository:

```bash
cd /home/eouser/projects/
```

3. Use the `git clone` command to clone the repository:

```bash
git clone https://github.com/JessBurEum/bids25.git
```

4. Verify that the repository was cloned successfully:

```bash
ls /home/eouser/projects/bids25
```

You should see the files and folders from the repository.

---

## Notes

- Ensure that Git is installed on your VM. You can check by running:

```bash
git --version
```

- If the `/home/eouser/projects/` directory does not exist, create it first:

```bash
mkdir -p /home/eouser/projects/
```

---

## Expected Outcome

After completing this exercise, the `bids25` repository should be cloned in:

```
/home/eouser/projects/bids25
```
You will use this repository in the following exercises.
