from flask import Flask, render_template, request, jsonify
import pandas as pd


app = Flask(__name__)

# Define the Excel file
FILE_NAME = 'Components.xlsx'


# Helper functions to load and save data
def load_data():
    try:
        data = pd.read_excel(FILE_NAME)
        data.columns = data.columns.str.strip()  # Clean column names
        return data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        raise

def save_data(df):
    try:
        df.to_excel(FILE_NAME, index=False)
    except Exception as e:
        print(f"Error saving Excel file: {e}")
        raise

# Home route to render the HTML page
@app.route('/')
def index():
    try:
        data = load_data()
        companies = data['Company name'].unique().tolist()  # Get unique company names
        return render_template('track.html', companies=companies)
    except KeyError as e:
        return f"KeyError: {e}. Please ensure the Excel file has the correct column names."

# Route to update the quantity of packets
@app.route('/update_packets', methods=['POST'])
def update_packets():
    try:
        company = request.form['company']
        component = request.form['component']
        value = request.form['value']
        packet_change = int(request.form['packet_change'])

        # Load the data and find the matching row
        data = load_data()
        row_index = data[
            (data['Company name'] == company) &
            (data['Components'] == component) &
            (data['Values'] == value)
        ].index

        if not row_index.empty:
            # Update the 'Packets' column
            data.loc[row_index, 'Packets'] += packet_change
            save_data(data)
            new_balance = data.loc[row_index, 'Packets'].values[0]
            message = f"Updated {component} for {company}. New balance: {new_balance} packets."
        else:
            message = "No matching component found to update."

        return jsonify({'message': message})
    except KeyError as e:
        return jsonify({'error': f"KeyError: {e}. Please check your Excel file for the correct column names."})
    except ValueError:
        return jsonify({'error': "Invalid packet change value. Please enter a number."})

if __name__ == '__main__':
    app.run(debug=True)
