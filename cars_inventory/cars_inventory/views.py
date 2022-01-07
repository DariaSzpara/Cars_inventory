class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

    def get_queryset(self):
        return Cars.objects.annotate(
           #make = Count('trucks'),
            #model = Sum('trucks__capacity')

    
