from django import forms
from catalog.models import BlogPost, Product, Version


class BlogPostFilterForm(forms.Form):
    is_published = forms.BooleanField(label='Только опубликованные', required=False)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'preview': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ['name', 'description', 'preview_image', 'category', 'price', 'is_published']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'preview_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        for word in self.FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise forms.ValidationError('Имя содержит запрещенное слово: {}'.format(word))

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')

        for word in self.FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise forms.ValidationError('Описание содержит запрещенное слово: {}'.format(word))

        return description


class ProductVersion(forms.ModelForm):
    DELETE = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Version
        fields = ('product', 'version_number', 'version_name', 'is_active', 'DELETE')
        widgets = {
            'version_number': forms.TextInput(attrs={'class': 'form-control'}),
            'version_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_version_name(self):
        version_name = self.cleaned_data.get('version_name')

        for word in ProductForm.FORBIDDEN_WORDS:
            if word.lower() in version_name.lower():
                raise forms.ValidationError('Название версии содержит запрещенное слово: {}'.format(word))

        return version_name

    def clean_is_active(self):
        is_active = self.cleaned_data.get('is_active')
        if is_active:
            active_count = self.instance.product.version_set.filter(is_active=True).count()
            print(active_count)
            if active_count > 0 and not self.instance.is_active:
                raise forms.ValidationError('Может быть только одна активная версия продукта.')
        return is_active

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            count_active = len([f for f in formset if f.cleaned_data.get('is_active') is True])
            if count_active <= 1:
                self.object = form.save()
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)

class ProductFilterForm(forms.Form):
    is_published = forms.BooleanField(label='Только активные', required=False)
