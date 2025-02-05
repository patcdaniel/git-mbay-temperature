# Monterey Bay Aquarium Seawater Intake Temperature

Contributors (Add Your Name Here):
Patrick Daniel -




## Project Overview

This project analyzes the seawater intake temperature data from the Monterey Bay Aquarium. The goal is to understand temperature trends and their potential impact on marine life.

## Data

The dataset includes daily temperature readings from the seawater intake system at the Monterey Bay Aquarium. The data spans multiple years and is stored in a CSV file.

## Installation

To run the analysis, you will need to install the following dependencies:

```bash
pip install pandas matplotlib
```

## Usage

To perform the analysis, you will first need to download the data from the CeNCOOS ERDDAP server.

__Download Data__
```bash
./src/download_data.sh
```
__Generate Figures__
```bash
python analyze_temperature.py
```

## Results

The results of the analysis will be saved in the `results` directory, including plots. Two plots are generate. First a timeseries of sea water temeperature with a 40 hour 'hann' low pass filter applied. Second, a scatter plot of temperature and dissolved oxygen saturation.

--- 

## Contributing

You task, should you choose to accept, is to make to `fork` this repository.

### Step 1: Fork the Repository

1. Navigate to the GitHub repository you want to contribute to.
2. Click the **Fork** button at the top-right corner of the page.
3. This creates a copy of the repository under your GitHub account.

### Step 2: Clone the Repository

1. Open a terminal or command prompt.
2. Run the following command to clone the repository to your local machine:

   ```sh
   git clone https://github.com/YOUR-USERNAME/git-mbay-temperature.git
   ```
3. Navigate into the project directory:

   ```sh
   cd git-mbay-temperature
   ```

## Step 3: Create a New Branch

1. Before making changes, create a new branch:

   ```sh
   git checkout -b your-branch-name
   ```

2. Use a descriptive name for your branch, such as `fix-bug-123` or `add-feature-x`.

## Step 4: Make Your Changes

1. Open the __THIS FILE__ (README.md) in your preferred code editor.
2. Add your Name and your email (formatted for markdown)
3. Save your changes.

## Step 5: Commit Your Changes

1. Stage your changes:

   ```sh
   git add .
   ```

2. Commit your changes with a meaningful message:

   ```sh
   git commit -m "Add your message here"
   ```

## Step 6: Push Your Changes

1. Push your changes to your forked repository:

   ```sh
   git push origin your-branch-name
   ```

## Step 7: Create a Pull Request (PR)

1. Navigate to your forked repository on GitHub.
2. Click the **Compare & pull request** button.
3. Provide a meaningful title and description for your changes.
4. Click **Create pull request**.

## Step 8: Address Feedback

1. The project maintainers may review your pull request and request changes.
2. If needed, update your branch:

   ```sh
   git add .
   git commit -m "Address feedback from maintainers"
   git push origin your-branch-name
   ```

3. Your PR will update automatically with your new commits.

## Step 9: Merge Your Changes (If Approved)

1. Once approved, the maintainers will merge your pull request.
2. You can delete your branch locally and remotely:

   ```sh
   git branch -d your-branch-name
   git push origin --delete your-branch-name
   ```

## Step 10: Keep Your Fork Updated

1. Switch to the main branch:

   ```sh
   git checkout main
   ```

2. Add the original repository as an upstream remote:

   ```sh
   git remote add upstream https://github.com/patcdaniel/git-mbay-temperature
   ```

3. Fetch the latest changes:

   ```sh
   git fetch upstream
   ```

4. Merge the changes:

   ```sh
   git merge upstream/main
   ```

5. Push the updates to your fork:

   ```sh
   git push origin main
   ```

## Conclusion

Congratulations!🎉You have successfully contributed to an open-source project.🎉


## License

This project is licensed under the MIT License.