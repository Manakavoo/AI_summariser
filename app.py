from flask import Flask, render_template, request, jsonify

from text_summarization import extractive_sum
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    # Get data from frontend

    print("connected to summarize")
    data = request.json
    
    text = data.get('text', '')
    summary_type = data.get('type')
    summary_size = data.get('size')
    print(summary_type,summary_size)
    # Placeholder for actual summarization logic
    if not text:
        return jsonify({
            'error': 'No text provided',
            'summary': ''
        }), 400
    
    # Simulated summarization (replace with actual implementation)
    if summary_type == 'extractive':
        # Simulate extractive summary
        # words = text.split()
        # num_words = max(10, int(len(words) * (int(summary_size) / 100)))
        # summary = ' '.join(words[:num_words])

        summary = extractive_sum(text,summary_percentage=int(summary_size))
    elif summary_type == 'abstractive':
        # Simulate abstractive summary
        # words = text.split()
        # num_words = max(10, int(len(words) * (int(summary_size) / 100)))
        # summary = ' '.join(words[:num_words]) + '...'

        summary = extractive_sum(text,summary_percentage=int(summary_size))
    else:
        return jsonify({
            'error': 'Invalid summary type',
            'summary': ''
        }), 400
    
    return jsonify({
        'summary': summary,
        'original_length': len(text.split()),
        'summary_length': len(summary.split())
    })



if __name__ == '__main__':
    app.run(debug=True)