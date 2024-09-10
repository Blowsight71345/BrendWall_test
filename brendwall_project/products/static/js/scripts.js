const form = document.getElementById('product-form');
const productBody = document.getElementById('product-body');

const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

async function fetchProducts() {
    try {
        const response = await fetch('/api/products/');
        if (!response.ok) {
            throw new Error('Ошибка сети');
        }
        const data = await response.json();
        productBody.innerHTML = '';
        data.forEach(product => {
            const row = `<tr>
                <td>${product.name}</td>
                <td>${product.description}</td>
                <td>${product.price}</td>
            </tr>`;
            productBody.innerHTML += row;
        });
    } catch (error) {
        console.error('Ошибка при загрузке продуктов:', error);
    }
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const price = parseFloat(document.getElementById('price').value);

    const response = await fetch('/api/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ name, description, price }),
    });

    if (response.ok) {
        document.getElementById('product-form').reset();
        await fetchProducts();
    } else {
        const errorData = await response.json();
        alert(`Ошибка: ${errorData.detail || 'Неизвестная ошибка.'}`);
    }
});

fetchProducts();
