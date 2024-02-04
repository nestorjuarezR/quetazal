from decimal import Decimal
from store.models import Articulo
import copy


class Cart():

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('session_key')

        # Nuevo usuario le genera una session_key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart
        
    def add(self, product, product_qty):
    
        product_id = product.id
        
        if product_id in self.cart:
            self.cart[product_id]['id'] = product_id
        else:
            self.cart[product_id] = {'price': str(product.precio), 'qty': product_qty}
        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
    

    def __iter__(self):
        all_products_ids = self.cart.keys()
        products = Articulo.objects.filter(id__in=all_products_ids)

        cart = copy.deepcopy(self.cart)

        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item

    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())


    #Eliminar articulos del carrito
    def delete(self ,product):
        product_id= str(product)

        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

            #Actualizar cantidad
    def update(self, product, qty):
        product_id = str(product)
        product_quantity = qty

        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity
        self.session.modified = True
